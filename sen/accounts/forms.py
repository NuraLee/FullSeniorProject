from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MaterialInfo, User, Material

class MaterialSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)
    
    subject_choices = [
        ('', 'Not selected'),
        ('Art', 'Art'),
        ('Math', 'Math'),
        ('History', 'History'),
        ('Languages', 'Languages'),
        ('Science', 'Science'),
        ('Biology', 'Biology'),
        ('Computers', 'Computers'),
    ]
    
    grade_choices = [(str(i), str(i)) for i in range(1, 13)]
    grade_choices.insert(0, ('', 'Not selected'))  # Add "Not selected" as the first choice
    grade = forms.ChoiceField(choices=grade_choices, required=False)

    rating_choices = [(str(i), str(i)) for i in range(1, 6)]
    rating_choices.insert(0, ('', 'Not selected'))  # Add "Not selected" as the first choice
    rating = forms.ChoiceField(choices=rating_choices, required=False)

    subject = forms.ChoiceField(choices=subject_choices, required=False)


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('phone', 'first_name', 'last_name', 'email')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'subject', 'grade', 'pdf_file', 'description']
        

class MaterialRejectionForm(forms.Form):
    reason = forms.CharField(max_length=2550)


class CommentForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    user_rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating')
    user_comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Comment')

    class Meta:
        model = MaterialInfo
        fields = ['user_rating', 'user_comment']