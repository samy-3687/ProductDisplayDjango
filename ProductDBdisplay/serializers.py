from rest_framework import serializers
from ProductDBdisplay.models import Productmodel

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model= Productmodel
        fields= '__all__'