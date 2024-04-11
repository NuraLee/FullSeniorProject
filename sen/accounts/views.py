import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Prefetch, Case, When, IntegerField, Avg, F
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Material, MaterialRejection, Room, RoomMessage, User, MaterialInfo, FavoriteMaterial
from .serializers import MaterialSerializer, MaterialInfoSerializer, MaterialRejectionSerializer, RoomMessageSerializer, FavoriteMaterialSerializer
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import CommentForm, CustomUserCreationForm, MaterialForm, MaterialRejectionForm, MaterialSearchForm

@api_view(['GET', 'POST'])
@login_required
def my_materials(request):
    if request.method == 'GET':
        materials = Material.objects.filter(author=request.user)
        serializer = MaterialSerializer(materials, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.author = request.user
            material.save()
            return JsonResponse({'message': 'Material created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)

@api_view(['GET'])
@login_required
def home(request):
    search_form = MaterialSearchForm(request.GET)
    materials = Material.objects.annotate(
        views=Count('infos')
    ).select_related('author').order_by('-status', '-pk')
    user = request.user

    if user.role == User.Role.CUSTOMER:
        materials = materials.filter(
            status=Material.Status.VERIFIED,
            rating__gte=settings.MATERIAL_MIN_RATING,
            views__gte=settings.MATERIAL_MIN_VIEWS
        )
    elif user.role == User.Role.EXPERT:
        materials = materials.filter(status=Material.Status.NEW)

    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        selected_subject = search_form.cleaned_data.get('subject')
        selected_grade = search_form.cleaned_data.get('grade')
        selected_rating = search_form.cleaned_data.get('rating')

        if selected_subject:
            if selected_subject != '':
                materials = materials.filter(subject=selected_subject)

        if selected_grade:
            if selected_grade != '':
                materials = materials.filter(grade=selected_grade)

        if selected_rating:
            if selected_rating != '':
                materials = materials.filter(rating=selected_rating)

        if search_query:
            materials = materials.filter(title__icontains=search_query)

    serializer = MaterialSerializer(materials, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@login_required
def green_page(request):
    search_form = MaterialSearchForm(request.GET)
    materials = Material.objects.filter(
        status=Material.Status.VERIFIED
    ).annotate(
        views=Count('infos')
    ).select_related('author').order_by('-status', '-pk')

    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        selected_subject = search_form.cleaned_data.get('subject')
        selected_grade = search_form.cleaned_data.get('grade')
        selected_rating = search_form.cleaned_data.get('rating')

        if selected_subject:
            if selected_subject != '':
                materials = materials.filter(subject=selected_subject)

        if selected_grade:
            if selected_grade != '':
                materials = materials.filter(grade=selected_grade)

        if selected_rating:
            if selected_rating != '':
                materials = materials.filter(rating=selected_rating)

        if search_query:
            materials = materials.filter(title__icontains=search_query)

    serializer = MaterialSerializer(materials, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@login_required
def verify_material(request, material_pk):
    if request.user.role != User.Role.EXPERT:
        return JsonResponse({'error': 'User is not authorized to verify materials.'}, status=403)

    material = get_object_or_404(Material, pk=material_pk)
    material.status = Material.Status.VERIFIED
    material.save()
    return JsonResponse({'message': 'Material verified successfully'})

@api_view(['POST'])
@login_required
def reject_material(request, material_pk):
    if request.user.role != User.Role.EXPERT:
        return JsonResponse({'error': 'User is not authorized to reject materials.'}, status=403)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    form = MaterialRejectionForm(data)
    if form.is_valid():
        material = get_object_or_404(Material, pk=material_pk)
        rejection_reason = form.cleaned_data['reason']
        rejection, created = MaterialRejection.objects.get_or_create(
            material=material, expert=request.user)
        rejection.description = rejection_reason
        rejection.save()
        material.status = Material.Status.REJECTED
        material.save(update_fields=['status'])
        return JsonResponse({'message': 'Material rejected successfully.'})
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

@api_view(['GET', 'POST'])
@login_required
def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'GET':
        serializer = MaterialSerializer(material)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            material_info, _ = MaterialInfo.objects.get_or_create(
                material=material, user=request.user)

            material_info.user_comment = form.cleaned_data['user_comment']
            material_info.user_rating = form.cleaned_data['user_rating']
            material_info.commented_at = timezone.now()
            material_info.save()

            infos = MaterialInfo.objects.filter(material=material).exclude(commented_at__isnull=True).aggregate(
                avg_rating=Avg('user_rating')
            )
            material.rating = infos['avg_rating']
            material.save(update_fields=['rating'])

            serializer = MaterialInfoSerializer(material_info)
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)

@api_view(['GET'])
@login_required
def rejections(request):
    materials = Material.objects.annotate(
        views=Count('infos')
    ).prefetch_related(
        'rejections'
    ).filter(
        author=request.user, status=Material.Status.REJECTED
    ).all()

    serializer = MaterialSerializer(materials, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@login_required
def add_to_favorites(request, pk):
    material = get_object_or_404(Material, pk=pk)
    
    # Check if the material is already in favorites
    if request.user.favorite_materials.filter(material=material).exists():
        return JsonResponse({'error': 'This material is already in your favorites.'}, status=400)
    else:
        # Add material to favorites
        favorite_material = FavoriteMaterial.objects.create(user=request.user, material=material)
        return JsonResponse({'message': f"{material.title} has been added to your favorites."}, status=201)

@api_view(['GET'])
@login_required
def favorite_materials(request):
    favorite_materials = request.user.favorite_materials.all()
    serializer = FavoriteMaterialSerializer(favorite_materials, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
@login_required
def remove_from_favorites(request, favorite_material_id):
    favorite_material = get_object_or_404(FavoriteMaterial, pk=favorite_material_id)
    
    if favorite_material.user != request.user:
        return JsonResponse({'error': 'You are not authorized to remove this material from favorites.'}, status=403)
    else:
        favorite_material.delete()
        return JsonResponse({'message': 'Material removed from favorites successfully.'})

@api_view(['GET'])
@login_required
def room(request):
    room, _ = Room.objects.select_related('customer').get_or_create(customer_id=request.user.pk)
    room_messages = RoomMessage.objects.order_by('-created_at').annotate(author_username=F('author__username')).filter(room_id=room.pk).order_by('-created_at')[:settings.LAST_N_MESSAGE][::-1]

    serializer = RoomMessageSerializer(room_messages, many=True)
    return JsonResponse(serializer.data, safe=False)
