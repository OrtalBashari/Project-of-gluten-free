from dataclasses import field
from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Preferences, Comment, Recipe, CommentRecipe

class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    
    class Meta:
        model = Profile
        fields = ['profile_picture']

    def save(self, commit=True):
        user = self.instance.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            super().save(commit=commit)
        return user
                 
            
    
class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = [ 'preferences','favorite_recipes']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','description', 'ingredients','instructions', 'image']

        labels = {
            'name': 'שם המתכון',
            'description': 'תיאור',
            'ingredients': 'רכיבים',
            'instructions': 'הוראות הכנה',
            'image': 'תמונה',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'instructions': forms.Textarea(attrs={'rows': 4}),
        }
   


class Comment_RecipeForm(forms.ModelForm):
    class Meta:
        model = CommentRecipe
        fields = ['body']
        widgets = {
            'body' : forms.Textarea(attrs={'placeholder': 'add comment..'})

        }

        labels = {
            'body': ''
        }
