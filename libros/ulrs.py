from django.urls import path
from .utils import cantidad_palabras, ordenar_lista

urlpatterns = [
        path('contar-palabras/', cantidad_palabras, name='contar_palabras'),
        path('ordenar_lista/', ordenar_lista, name='ordenar_lista'),
]
 