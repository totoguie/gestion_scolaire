# Generated by Django 2.2.14 on 2022-01-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='matricule',
            field=models.CharField(max_length=10),
        ),
    ]
