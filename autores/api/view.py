from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
import os
from autores.api.serializer import AutoresSerializer, tareasSerializer

from autores.models import autores, tareas

class autoresApiViewSet(ModelViewSet):
    serializer_class = AutoresSerializer
    queryset = autores.objects.all()

class tareasApiViewSet(ModelViewSet):
    serializer_class = tareasSerializer
    queryset = tareas.objects.all()
    
    @action(detail=False, methods=["post"], url_path="crear-tarea")
    def crear_tarea(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda la tarea
            return Response(
                {"status": 1, "message": "Tarea creada correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="tareas")
    def listar_tareas(self, request):
        tareas = self.queryset
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="tarea")
    def obtener_tarea(self, request, pk=None):
        try:
            tarea = self.get_object()
            serializer = self.get_serializer(tarea)
            return Response(serializer.data)
        except tareas.DoesNotExist:
            return Response(
                {"status": 0, "message": "Tarea no encontrada"},
                status=status.HTTP_404_NOT_FOUND,
            )

    @action(detail=True, methods=["put"], url_path="actualizar-tarea")
    def actualizar_tarea(self, request, pk=None):
        tarea = self.get_object()
        serializer = self.get_serializer(tarea, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": 1, "message": "Tarea actualizada correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"], url_path="eliminar-tarea")
    def eliminar_tarea(self, request, pk=None):
        tarea = self.get_object()
        tarea.delete()
        return Response(
            {"status": 1, "message": "Tarea eliminada correctamente"},
            status=status.HTTP_204_NO_CONTENT,
        )