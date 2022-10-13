from dataclasses import fields
from teacher.models import Aula, Professor
from rest_framework import serializers
from django.forms import ValidationError

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CadastrarAulaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)
    
    # Validar tamanho do nome recebido
    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError('deve ter pelo menos três caracteres')
        return value

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'