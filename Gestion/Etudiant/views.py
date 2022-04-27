from django.shortcuts import render

# Create your views here.
def dashbord_etudiant(request):
    return render(request ,'stocks/dashbord_etudiant.html')