from django import forms


#se utiliza todo esto para validar los formularios 

class Profesores_formulario(forms.Form):

    nombre= forms.CharField(max_length=40) 
    apellido= forms.CharField(max_length=40) 
    disciplina= forms.CharField(max_length=40) 

class Alumnos_formulario(forms.Form):

    nombre= forms.CharField(max_length=40) 
    apellido= forms.CharField(max_length=40) 
    disciplina=forms.CharField(max_length=40)
    clasesMes=forms.IntegerField()
   

class Disciplinas_formulario(forms.Form):

    disciplina= forms.CharField(max_length=40) 
    dias=forms.CharField(max_length=40)