from django.urls import path
from . import views

urlpatterns = [

    #path de pantalla de inicio
    path("", views.inicio, name="inicio"),

    #path para ver y dar de alta los profesores
    path("profesores",views.profesores),
    path("alta_profesores", views.alta_profesores, name="profesores"),

    #path para ver y dar de alta los alumnos
    path("alumnos",views.alumnos),
    path("alta_alumnos", views.alta_alumnos, name="alumnos"),

    #path para ver y dar de alta las disciplinas
    path("disciplinas",views.disciplinas),
    path("alta_disciplina", views.alta_disciplinas, name="disciplinas"),
    
    
]