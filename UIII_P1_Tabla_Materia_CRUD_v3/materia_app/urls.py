from django.urls import path
from materia_app import views

urlpatterns = [
    path("",views.inicio_vista, name="inicio_vista"),
    path("registrarMateria/",views.registrarMateria,name="registrarMateria"),
    path("borrarMateria/<codigo>",views.borrarMateria,name="borrarMateria"),
    path("editarMateria/<codigo>",views.borrarMateria,name="editarmateria"),
    path("borrarMateria/<codigo>",views.borrarMateria,name="borrarMateria"),
]
