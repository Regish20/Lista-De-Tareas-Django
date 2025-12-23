from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=False)
    descripcion = models.TextField()
    importancia = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        if self.importancia == True:
            importanciaMensaje = "Es importante"
        else:
            importanciaMensaje = "No es importante"
        return self.nombre + " - " + self.usuario.username + " - " + importanciaMensaje