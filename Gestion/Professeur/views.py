from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Professeur
from .forms import profForm
from django.core.mail import send_mail
import random
# Create your views here.
# def pwd():
#     code=[]
#     for i in range(7):
#         cd=str(random.randint(0,9))
#         code.append(cd)
#         code_valide=("" .join(code))
#     return code_valide

def reset_pwd(request ):
    if request.method=='POST':
        mail = request.POST['email']
        if Professeur.objects.filter(mail=mail).exists():
            code=[]
            for i in range(7):
                cd=str(random.randint(0,9))
                code.append(cd)
                code_valide=("" .join(code))
            send_mail(
            'Reset your password' ,
            "Bonjour  votre mot de passe de réinitialisataion est {} .".format(code_valide),
            'smcorneille@gmail.com',
            ['{}'.format(mail)],
            fail_silently=False,
            )
            return redirect('verification',code_valide)
        else:
            messages.error(request ,"Adresse introuvable ! , veillez réessayer")
    return render(request ,'password_resset.html')

def verification(request ):
    if request.method=='POST':
        code=request.POST['code']
    else:
        messages.error(request ,'le code saisi est invalide ,réessayer')
    return render(request ,'verification.html')

def confirm(request ):
    return render(request ,'update_pwd.html')


login_required(login_url='login')
def dash(request):
   # mail=Professeur.objects.get(mail=mail)
    return render(request ,'navbar/dashbord.html')
#templates dans le dossier fiiere
#seg
def liste_seg(request):
    return render(request ,'filiere/liste_seg.html')
#fba
def liste_fba(request):
    return render(request ,'filiere/liste_fba.html')
#acg
def liste_acg(request):
    return render(request ,'filiere/liste_acg.html')
#igl
def liste_igl(request):
    return render(request ,'filiere/liste_igl.html')
#rit
def liste_rit(request):
    return render(request ,'filiere/liste_rit.html')
#finance compta
def liste_fc(request):
    return render(request ,'filiere/liste_fc.html')
#droit
def liste_droit(request):
    return render(request ,'filiere/liste_droit.html')

def login_prof(request):
    form=profForm(request.POST)
    if request.method =="POST":
         if form.is_valid():
            email=form.cleaned_data['mail']
            password=form.cleaned_data['password']
            for object in Professeur.objects.all():
                if object.mail==email and object.password==password:
                    request.session['email'] = email
                    return redirect('dashbord')
                else:
                    messages.error(request,"votre mail ou mot de passe incorrecte !")
                    form=profForm()
    return render(request ,'connexion.html',{'form':form})

def logout_prof(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('login')