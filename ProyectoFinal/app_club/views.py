from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_club.models import Profesores,Alumnos,Disciplinas
from app_club.forms import Profesores_formulario, Alumnos_formulario, Disciplinas_formulario

def inicio(request):
    return render( request, 'index.html' )


#PROFESORES BUSQUEDA Y ALTAS

def profesores(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']

        #cargo toda la base de datos de Curso y si encuentra el nombre que buscamos
        profesor= Profesores.objects.filter(nombre__icontains = nombre)

        return render(request, 'profesores.html' ,{"nombre":profesor})

    else:
        return HttpResponse("campo vacio")

def alta_profesores(request):
   
    if request.method == "POST":         
        mi_formulario = Profesores_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesor =Profesores(nombre=datos['nombre'], apellido=datos['apellido'], disciplina=datos['disciplina'])
            profesor.save() 
            return render(request,"profesores.html")
    
    
    return render(request,"profesores.html")


#ALUMNOS BUSQUEDA Y ALTAS

def alumnos(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']

        #cargo toda la base de datos de Curso y si encuentra el nombre que buscamos
        alumno= Alumnos.objects.filter(nombre__icontains = nombre)

        return render(request, 'alumnos.html' ,{"nombre":alumno})

    else:
        return HttpResponse("campo vacio")

def alta_alumnos(request):

    if request.method == "POST": 
        mi_formulario = Alumnos_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumno =Alumnos(nombre=datos['nombre'], apellido=datos['apellido'], disciplina=datos['disciplina'], clasesMes=datos['clasesMes'])
            alumno.save() 
            return render(request, "alumnos.html")
        
   

    return render(request, "alumnos.html")




#DISCIPLINAS BUSQUEDA Y ALTAS



def disciplinas(request):
    if request.GET['disciplina']:
        disciplina=request.GET['disciplina']
        disciplinas= Disciplinas.objects.filter(disciplina__icontains = disciplina)

        return render(request, 'disciplinas.html' ,{ "disciplina":disciplinas})

    else:
        return HttpResponse("campo vacio")
    
    


def alta_disciplinas(request):

    if request.method == "POST": 
       
        mi_formulario = Disciplinas_formulario(request.POST)
        
        if mi_formulario.is_valid():            
            datos=mi_formulario.cleaned_data
            disciplinas =Disciplinas(disciplina=datos ['disciplina'], dias=datos['dias'])
            disciplinas.save() 
            return render(request, "disciplinas.html")

    return render(request, "disciplinas.html")

        