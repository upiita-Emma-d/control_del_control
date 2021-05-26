from rest_framework import serializers

class HelloSeriealizer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)

class DATA(serializers.Serializer):
    name = serializers.CharField(max_length = 20000)    