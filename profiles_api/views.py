#from django.shortcuts import render
from rest_framework.utils.serializer_helpers import JSONBoundField
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
import json

class HelloApiView(APIView):
    ''' Creacion de API de prueba'''
    serializer_class = serializers.HelloSeriealizer
    def get(self,request, format = None):
        ''' Retornar lista de carcteristicas del APIView'''
        an_apiview = [
            'Usamos etodos de HTTP como funciones (get,post,path,put,delete)',
            'Es similar a una vista traciocional de Django',
            'Nos da el mayoe control sobre la logica de nuetro aplicacion',
            'Esta mapeado manuelaen a los URL',
        ]
        return Response({'mesaje':'Hello','an_apiview' : an_apiview})

    def post(self,request):
        ''' Crear un mensaje con nuestro nombre'''
        print(request.data)
        serializer = self.serializer_class(data = request.data)
        #print(serializer.validated_data.get('name'))
        if serializer.is_valid():
            name  = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk = None):
        ''' MAjena actalizar un objeto '''
        return Response({'method':'PUT'})

    def patch(self,request,pk = None):
        return Response({'Method': 'PATHC'})

    
    def delete(self,request,pk = None):
        return Response({'Method': 'DELETE'}) 

# Create your views here.
class DATOS(APIView):
    ''' Creacion de API de prueba'''
    serializer_class = serializers.HelloSeriealizer
    def get(self,request, format = None):
        ''' Retornar lista de carcteristicas del APIView'''
        an_apiview = [
            'Usamos etodos de HTTP como funciones (get,post,path,put,delete)',
            'Es similar a una vista traciocional de Django',
            'Nos da el mayoe control sobre la logica de nuetro aplicacion',
            'Esta mapeado manuelaen a los URL',
        ]
        return Response({'mesaje':'Hello','an_apiview' : an_apiview})

    def post(self,request):
        ''' Crear un mensaje con nuestro nombre'''
        el_dic = request.data
        #for valores in el_dic['ADC']:
         #   print(valores)

        return Response({'ESTADO : OK'})
