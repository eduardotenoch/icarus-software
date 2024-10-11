from rest_framework import serializers
from libros.models import libros


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = libros
        fields = "__all__"
