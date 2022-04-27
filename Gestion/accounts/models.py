from django.db import models

# Create your models here.
class Etudiant(models.Model) :
    username = models.CharField(max_length=15,verbose_name='Username')
    prenom = models.CharField(max_length=20,verbose_name='Prenom')
    email= models.EmailField(verbose_name='Email')
    matricule=models.CharField(max_length=10)
    numero = models.CharField(max_length=15,verbose_name='Numero')
    Genre =(('M','Masculin'),('F','Feminin'))
    genre = models.CharField(max_length=1, choices=Genre ,verbose_name='Genre')
    
    def __str__(self):
        return self.username

class Professeur(models.Model):
    nom=models.CharField(max_length=25)
    prenom=models.CharField(max_length=30)
    sexe = models.CharField(blank=True, null=True,
                            choices=(('Homme', 'Homme'), ('Femme', 'Femme')), max_length=256)
    mail=models.EmailField()
    password=models.CharField(max_length=10)
    tel=models.CharField(max_length=10)

    def __str__(self):
        return self.nom +" " + self.prenom