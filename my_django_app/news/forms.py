from dataclasses import fields
from .models import Articles,Logs
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinValueValidator

from django.forms import ModelForm,TextInput,DateTimeInput,Textarea,ImageField,FileField


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields='__all__'
        
        widgets={
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Тағам аты'
            }),
            "anons":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Сипаттамасы'
            }),
            "date":DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Жариялаған күні'
            }),
            "full_text":Textarea(attrs={
                'class':'form-control',
                 'placeholder':'Толық сипаттамасы' 
            })
            } 

class CreateUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=100)
    age=forms.CharField(max_length=100)

    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name','phone','age']

class Logreg(forms.ModelForm):
    class Meta:
        model = Logs
        fields = ['username','email','password1','password2','first_name','last_name','phone','age']

class ContactForm(forms.Form):
    subject=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows": 5}))
        