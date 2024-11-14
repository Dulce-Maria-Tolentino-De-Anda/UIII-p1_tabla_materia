from django.shortcuts import redirect, render
from .models import Materia

# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credito=request.POST["numcredito"]

    guardarmateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,credito=credito
    ) # guarda el registro

    return redirect("/")
def seleccionarMateria(request,codigo):
    materia=materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html", {"mismateria":materia})

def editarMateria(request,):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtcodigo"]
    credito=request.POST["txtcodigo"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.credito=credito
    materia.save() #guardar regristro actualizado

def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete() #borra el registro
    return redirect("/")

