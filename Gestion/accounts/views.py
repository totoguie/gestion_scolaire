# Create your views here.
from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import Etudiant ,Professeur
from django.core.mail import send_mail
import random

from .forms import EtudiantForm ,ResetForm

def login_user(request):
    forms=EtudiantForm(request.POST)
    if request.method =="POST":
         if forms.is_valid():
            username=forms.cleaned_data['username']
            matricule=forms.cleaned_data['matricule']
            for object in Etudiant.objects.all():
                if object.username==username and object.matricule==matricule:
                    request.session['username']=username
                    return redirect('d_etudiant')
                else:
                    messages.error(request,"Non d'utlisateur ou mot de passe incorrecte !")
                    forms=EtudiantForm()
    return render(request ,'login.html',{'forms':forms})

def logout_account(request):
    try :
        del request.session['username']
    except:
        pass
    return redirect('login')
