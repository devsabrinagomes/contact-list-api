from django.db import models
from uuid import uuid4

# Create your models here.
class Contato(models.Model):
    id_contato = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=50, unique=True)
    foto = models.FileField(upload_to='fotos/', null=True, blank=True)
    numero = models.CharField(max_length=14, unique=True)

    class Meta:
        ordering = ['nome']
