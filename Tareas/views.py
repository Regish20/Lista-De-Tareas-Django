from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Tarea
from django.contrib.auth import login, logout, authenticate
from .forms import FormTarea
from django.contrib.auth.decorators import login_required
# Create your views here.
def Inicio(request):
    return render(request, "inicio.html")
def Registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {
            "form" : UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                usuario = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                usuario.save()
                login(request, usuario)
                return redirect("Tareas")
            except:
                return render(request, "registro.html", {
                    "form" : UserCreationForm,
                    "error": "Error de creación de usuario"
                })
        else:
            return render(request, "registro.html", {
                    "form" : UserCreationForm,
                    "error": "Contraseña invaida"
                })

@login_required  
def Tareas(request):
    tareas_hechas = Tarea.objects.filter(usuario=request.user)
    return render(request, "tareas.html", {
        "tareas": tareas_hechas}
        )

@login_required
def crearTareas(request):
    if request.method == "GET":
        return render(request, "crearTareas.html", {
            "form": FormTarea
        })
    else:
        try:
            formulario = FormTarea(request.POST)
            nueva_tarea = formulario.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect("Tareas")
        except:
            return render(request, "crearTareas.html", {
                "form": FormTarea,
                "error": "Se ha registrado un error"
            })
    
@login_required
def detalleTarea(request, tarea_id):
    if request.method == "GET":
        tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
        formulario = FormTarea(instance=tarea)
        return render(request, "detalleTarea.html", {
                    "tarea": tarea,
                    "formulario": formulario
                })
    else:
        try:
            tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
            formulario = FormTarea(request.POST, instance=tarea)
            formulario.save()
            return redirect("Tareas") 
        except:
            return render(request, "detalleTarea.html", {
                    "tarea": tarea,
                    "formulario": formulario,
                    "error": "Hubo un error al actualizar la tarea"
                })

@login_required
def completarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    tarea.estado = True
    tarea.save()
    print(tarea)
    return redirect("Tareas")

@login_required
def eliminarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    tarea.delete()
    print(tarea)
    return redirect("Tareas")

@login_required
def CerrarSesion(request):
    logout(request)
    return redirect("Inicio")


def Logueo(request):
    if request.method == "GET":
        return render(request, "login.html", {
            "form": AuthenticationForm
        })
    else:
        try:
            usuario = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if usuario is None:
                return render(request, "login.html", {
                    "form": AuthenticationForm,
                    "error": "El usuario no ha sido registrado"
                })
            else:
                login(request, usuario)
                return redirect("Tareas")
        except:
            return render(request, "login.html", {
            "form": AuthenticationForm,
            "error": "Error al iniciar sesión"
            })