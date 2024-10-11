from django.urls import path
from rest_framework.routers import DefaultRouter

from autores.api.view import autoresApiViewSet, tareasApiViewSet

router_autores = DefaultRouter()

router_autores.register(prefix="autores", basename="autores", viewset=autoresApiViewSet)
router_autores.register(prefix="tareas", basename="tareas", viewset=tareasApiViewSet)