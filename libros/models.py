from django.db import models
from autores.models import autores

class libros(models.Model):
    titulo = models.CharField(max_length=40, null=False, blank=True)
    autor = models.ForeignKey(autores, on_delete=models.CASCADE, blank=True, null=True)
    fechapublicacion = models.TimeField(blank=True, null = False)
