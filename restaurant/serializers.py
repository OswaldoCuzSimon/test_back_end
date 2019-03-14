from decimal import Decimal

from django.contrib.gis.geos import GEOSGeometry
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    id = serializers.CharField(max_length=36)
    rating = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    site = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    location = serializers.SerializerMethodField()


    def get_location(self, obj):

        return {
                "lng": obj.location.x,
                "lat": obj.location.y
            }

    def to_internal_value(self, data):
        if 'location' in data:
            lat, lng = Decimal(data['location']['lat']), Decimal(data['location']['lng'])
            location = GEOSGeometry("POINT({0} {1})".format(lng, lat))
            data['location'] = location
        return data

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
        instance.location = validated_data.get('location', instance.location)

        instance.save()

        return instance
