from django.contrib import admin

# Register your models here.
from .models import Etudiant ,Professeur
admin.site.register(Etudiant)

admin.site.register(Professeur)