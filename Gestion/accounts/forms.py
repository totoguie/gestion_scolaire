from .models import Etudiant
from django.forms import ModelForm
from django import forms

class EtudiantForm(ModelForm):
    class Meta:
        model=Etudiant
        fields=['username' ,'matricule']
        widgets={
            'username':forms.TextInput(attrs={
                'placeholder':"username",
                'class':'form-control'
            }),
            'matricule':forms.PasswordInput(attrs={
                'placeholder':'password' ,
                'class':'form-control'
            })
        }

class ResetForm(ModelForm):
    class Meta:
        model=Etudiant
        fields=['username','matricule']
        widgets={
            'matricule1':forms.TextInput(attrs={
                'placeholder':"username",
                'class':'form-control'
            }),
            'matricule2':forms.PasswordInput(attrs={
                'placeholder':'password' ,
                'class':'form-control'
            })
        }