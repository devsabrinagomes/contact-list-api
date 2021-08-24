from rest_framework import serializers
from contatos import models

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contato
        fields = '__all__'
