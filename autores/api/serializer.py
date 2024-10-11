from rest_framework import serializers
from autores.models import autores, tareas


class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = autores
        fields = "__all__"
    
class tareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = tareas
        fields = "__all__"