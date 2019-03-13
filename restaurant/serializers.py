from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=36)
    rating = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    site = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lng = serializers.DecimalField(max_digits=9, decimal_places=6)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)
