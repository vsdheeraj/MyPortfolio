from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

# from datetime import datetime

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = { 
                   'tags' : forms.CheckboxSelectMultiple(),         
                   'github_url': forms.URLInput(attrs={
                       'placeholder': 'https://github.com/username/repo'
                   }),
                    # 'created' : forms.DateTimeInput(attrs={
                    #                                         'type':'datetime-local', 
                    #                                         'max': datetime.now().strftime('%Y-%m-%dT%H:%M')
                    #                                         }
                    #                                 ), 
                   }
        
        
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     # Automatically set the created field to the current date and time if not set
    #     if not instance.created:
    #         instance.created = datetime.now()
    #     if commit:
    #         instance.save()
    #     return instance