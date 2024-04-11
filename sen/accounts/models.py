import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


from django.contrib.auth.models import AbstractUser
from django.db import models

def pdf_file_path(instance, filename):
    return f'media/pdf_files/{filename}'

class User(AbstractUser):
    class Role(models.IntegerChoices):
        EXPERT = 1, "moderaot"
        CUSTOMER = 2, 'customer'
    
    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.CUSTOMER)
    phone = models.CharField(max_length=15)


    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'
    
    @property
    def is_customer(self):
        return self.role == User.Role.CUSTOMER
    
    @property
    def is_expert(self):
        return self.role == User.Role.EXPERT
    

class Material(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        VERIFIED = 'verified', 'Verified'
        REJECTED = 'rejected', 'Rejected'

    author = models.ForeignKey(User, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    pdf_file = models.FileField(
        upload_to=pdf_file_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    subject = models.CharField(max_length=20, default='algebra')
    grade = models.CharField(max_length=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def filename(self):
        return os.path.basename(self.pdf_file.name)
    
    @property
    def is_new(self):
        return self.status == Material.Status.NEW
    
    @property
    def created_at_with_timezone(self):
        return self.created_at.astimezone(timezone.get_current_timezone()).strftime('%d.%m.%Y %H:%M')
    
    def __str__(self) -> str:
        return self.title
    
class FavoriteMaterial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'material')    

class MaterialInfo(models.Model):
    material = models.ForeignKey('Material', related_name='infos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='material_infos', on_delete=models.CASCADE)
    user_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    user_comment = models.TextField(null=True, blank=True)
    commented_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['material', 'user']]

    def __str__(self):
        return f"Info for Material: {self.material.title}"
    
    @property
    def created_at_with_timezone(self):
        return self.created_at.astimezone(timezone.get_current_timezone()).strftime('%d.%m.%Y %H:%M')
    

class MaterialRejection(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='rejections')
    expert = models.ForeignKey(User, related_name='material_rejections', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        unique_together = [['material', 'expert']]

    def __str__(self):
        return f"Rejection for Material: {self.material.title}"
    
    @property
    def created_at_with_timezone(self):
        return self.created_at.astimezone(timezone.get_current_timezone()).strftime('%d.%m.%Y %H:%M')
    
    
class FavoriteMaterial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Room(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_rooms')
    name = models.CharField(max_length=100, null=True, blank=True)


class RoomMessage(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    response_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
