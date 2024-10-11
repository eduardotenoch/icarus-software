from django.db import models

class autores(models.Model):
    nombre = models.CharField(max_length=40, null=False, blank=True)
    fechaNacimiento =  models.DateField(blank=True, null=True)

class tareas(models.Model):
    nombretarea = models.CharField(max_length=40, null=False, blank=True)
    autor = models.ForeignKey(autores, on_delete=models.CASCADE, blank=True, null=True)
    fechatarea =  models.DateField(blank=True, null=True)
