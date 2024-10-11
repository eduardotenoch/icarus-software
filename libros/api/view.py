from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
import os

from libros.api.serializer import LibrosSerializer
from libros.models import libros

class LibrosApiViewSet(ModelViewSet):
    serializer_class = LibrosSerializer
    queryset = libros.objects.all()

    def ordenar_numeros(self, lista):
        return sorted(lista)

    @action(
        detail=False,
        methods=["put"],
        url_path=r"ordenar",
    )
    def ordenar(self, request):
        numeros = request.data.get('numeros', None)
        if numeros is None:
            return Response({"error": "No se proporcionaron números."}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(numeros, list):
            return Response({"error": "La entrada debe ser una lista."}, status=status.HTTP_400_BAD_REQUEST)

        sorted_numeros = self.ordenar_numeros(numeros)
        return Response(sorted_numeros, status=status.HTTP_200_OK)
    
    @action(
        detail=False,
        methods=["put"],
        url_path=r"contar_palabras",
    )
    def contar_palabras(self, request):  # Asegúrate de incluir 'self'
        archivo = request.FILES.get('archivo')  # Ajusta 'archivo' al nombre real de tu campo

        if archivo:
            # Extraer el nombre del archivo del objeto InMemoryUploadedFile
            nombre_archivo = archivo.name  # Obtener el nombre del archivo subido
            
            # Usar el nombre del archivo para crear la ruta completa
            ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
            
            # Guardar el archivo en el servidor
            with open(ruta_archivo, 'wb+') as destino:
                for chunk in archivo.chunks():
                    destino.write(chunk)

            # Contar las palabras en el archivo guardado
            total_palabras = self.contar_palabras_en_archivo(ruta_archivo)

            return Response({'mensaje': 'Palabras contadas exitosamente', 'total_palabras': total_palabras})
        else:
            # Manejar el caso donde no se subió ningún archivo
            return Response({'error': 'No se ha subido ningún archivo'}, status=400)

    def contar_palabras_en_archivo(self, ruta_archivo):
        """Cuenta el número de palabras en un archivo de texto."""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                # Contar las palabras, separadas por espacios
                palabras = contenido.split()
                return len(palabras)  # Retorna el número total de palabras
        except Exception as e:
            return 0  # Si hay un error, retorna 0 o maneja el error según sea necesario