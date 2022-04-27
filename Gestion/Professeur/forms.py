from accounts.models import  Professeur
from django.forms import ModelForm
from django import forms

class profForm(ModelForm):
    class Meta:
        model=Professeur
        fields=['mail' ,'password']
        widgets={
            'mail':forms.TextInput(attrs={
                'placeholder':"adresse mail",
                'class':'form-control'
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'password' ,
                'class':'form-control'
            })
        }