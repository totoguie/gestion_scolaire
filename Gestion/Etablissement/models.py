from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import CharField, IntegerField
# Create your models here.
from accounts.models import *
class Groupe(models.Model):
    nom_group=models.CharField(max_length=20)

class Niveau(models.Model):
    choix_niv=[
        ('niveau1','Licence1'),
        ('niveau2','Licence2'),
        ('niveau3','Licence3'),
        ('niveau4','Master1'),
        ('niveau5','Master2'),
        ]
    lib_niveau=models.CharField(choices=choix_niv, max_length=15)
    groupe=models.ForeignKey(Groupe,on_delete=models.CASCADE)

class Filiere(models.Model):
    choix_filiere=[ 
        ('filiere1','DROIT'),
        ('filiere2','SEG'),
        ('filiere3','FBA'),
        ('filiere4','FC '),
        ('filiere5','IGL '),
        ('filiere6',"ACG"),
        ('filiere7','RIT '),
        ]   
    libele_filiere= models.CharField(choices=choix_filiere, max_length=15)


class Departement(models.Model):
    libele=models.CharField(max_length=15)
    filiere=models.ForeignKey(Filiere,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    professeur=models.ManyToManyField(Professeur,through='Seance',related_name='professeur')
    niveau=models.ManyToManyField(Niveau,through='Matiere',related_name='niveau',)

class Seance(models.Model):
    salle=models.CharField(max_length=20)
    date=models.DateField()
    heure=models.DateTimeField()
    departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)

class Matiere(models.Model):
    libele=models.CharField(max_length=25)
    coefficient=models.IntegerField()    
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE)
    professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
    