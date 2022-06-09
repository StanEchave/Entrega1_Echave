from django.db import models

# Create your models here.

class Profesores(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40) 
    disciplina= models.CharField(max_length=40) 

class Alumnos(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40) 
    disciplina=models.CharField(max_length=40)
    clasesMes=models.IntegerField(null=0)
   
    
class Disciplinas(models.Model):
    disciplina= models.CharField(max_length=40) 
    dias=models.CharField(max_length=40)
