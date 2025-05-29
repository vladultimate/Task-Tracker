from django import forms
from .models import Board, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'priority', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class BoardEditingForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'priority', 'state', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишіть коментар...',
                'class': 'form-control rounded' 
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



class FilterForm(forms.Form):
    PRIORITY_CHOICES = [
    ('', 'Усі'),
    ('low', 'Низький'),
    ('medium', 'Середній'),
    ('high', 'Високий')]
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False, label='Пріоритет')