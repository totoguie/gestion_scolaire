from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Etudiant ,Professeur
# Create your views here.
login_required(login_url='login')
def index(request):
    #user=Etudiant.objects.get(uername=username)
    return render (request ,'temp/home.html')

def formation(request):
    return render(request, 'temp/formation.html')

def atout(request):
    return render(request ,'temp/nos_atout.html')

def sesion(request):
    return render(request ,'temp/session.html')

def details(request):
    return render(request ,'temp/details_filiere.html')