from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from contatos.models import Contato
from rest_framework import viewsets, status
from contatos.api import serializers

class ContatoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContatoSerializer
    queryset = Contato.objects.all()


    # def list(self, request, *args, **kwargs):
    #     try:
    #         contato = Contato.objects.all()
    #         serializers = self.serializer_class(contato, many=True)
    #         return Response(data=serializers.data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response(e, status=status.HTTP_400_BAD_REQUEST)
    #
    # def create(self, request, *args, **kwargs):
    #
    #     print(request.data)
    #
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def update(self, request, *args, **kwargs):
    #
    #     print(request.data)
    #     print(kwargs)
    #
    #     conta = Contato.objects.get(id_contato=kwargs['id_contato'])
    #     serializer = self.serializer_class(conta, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, *args, **kwargs):
    #
    #     print(kwargs)
    #
    #     try:
    #         contato = Contato.objects.filter(id_contato=kwargs['id_contato']).order_by(
    #             'nome')
    #         serializers = self.serializer_class(contato, many=False)
    #         return Response(data=serializers.data, status=status.HTTP_200_OK)
    #     except ObjectDoesNotExist:
    #         return Response({'message': 'Registro não existe!'}, status=status.HTTP_404_NOT_FOUND)