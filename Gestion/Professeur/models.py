from django.db import models

# Create your models here.

class cour(models.Model):
    titre= models.CharField(max_length=30)