from django.urls import path
from .views import Registro, Inicio, Tareas, CerrarSesion, Logueo, crearTareas, detalleTarea, completarTarea, eliminarTarea

urlpatterns = [
    path('Registro/', Registro, name="Registro"),
    path("", Inicio, name="Inicio"),
    path("Tareas/", Tareas, name="Tareas"),
    path("Tareas/Crear", crearTareas, name="Tareas/Crear"),
    path("Logout/", CerrarSesion, name="Logout"),
    path("Login/", Logueo, name="Login"),
    path("detalleTarea/<int:tarea_id>/", detalleTarea, name="detalleTarea"),
    path("detalleTarea/<int:tarea_id>/completarTarea", completarTarea, name="completarTarea"),
    path("detalleTarea/<int:tarea_id>/eliminarTarea", eliminarTarea, name="eliminarTarea")

] 