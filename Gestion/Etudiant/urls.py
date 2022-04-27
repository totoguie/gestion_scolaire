from os import name
from django.urls import path ,include
from .import views 
urlpatterns = [
    path('Dashbord_etudiant/',views.dashbord_etudiant ,name="d_etudiant")
]
