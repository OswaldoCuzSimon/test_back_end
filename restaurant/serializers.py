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

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.name = validated_data.get('name', instance.name)
        instance.site = validated_data.get('site', instance.site)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)

        instance.save()

        return instance
