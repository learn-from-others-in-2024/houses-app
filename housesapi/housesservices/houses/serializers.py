from rest_framework import serializers

from .models import House


# Creating serializer for the House model:
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
