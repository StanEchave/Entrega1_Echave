from django.urls import path
from . import views

urlpatterns = [

    #path de pantalla de inicio
    path("", views.inicio, name="inicio"),

    #path para ver y dar de alta los profesores
    path("profesores",views.profesores, name="profesores"),
    path("alta_profesor", views.alta_profesores),

    #path para ver y dar de alta los alumnos
    path("alumnos",views.alumnos, name="alumnos"),
    path("alta_alumno", views.alta_alumnos),

    #path para ver y dar de alta las disciplinas
    path("disciplinas",views.disciplinas, name="disciplinas"),
    path("alta_disciplina", views.alta_disciplinas),
]