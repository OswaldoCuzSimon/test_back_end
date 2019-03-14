from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RestaurantSerializer
from django.db.utils import IntegrityError
from .models import Restaurant
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import Distance
from decimal import Decimal
import numpy as np

class RestaurantView(APIView):
    def get(self, request):
        articles = Restaurant.objects.all()
        serializer = RestaurantSerializer(articles, many=True)
        return Response({"restaurants": serializer.data})

    def post(self, request):
        try:
            restaurant = request.data.get('restaurant')

            # Create an article from the above data
            serializer = RestaurantSerializer(data=restaurant)
            if serializer.is_valid(raise_exception=True):
                restaurant_saved = serializer.save()
            return Response({
                "success": "Restaurant '{}' created successfully".format(restaurant_saved.name)
            }, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response([{"id": "id must be unique"}], status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, restaurant_id):
        saved_restaurant = get_object_or_404(Restaurant.objects.all(), id=restaurant_id)
        data = request.data.get('restaurant')
        serializer = RestaurantSerializer(instance=saved_restaurant, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            restaurant_saved = serializer.save()

        return Response({"success": "Restaurant '{}' updated successfully".format(restaurant_saved.name)})

    def delete(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant.objects.all(), id=restaurant_id)
        restaurant.delete()
        return Response({"message": "Restaurant with id {} has been deleted.".format(restaurant_id)}, status=204)

class RestaurantStatistics(generics.ListAPIView):
    """
    This view should return statistics of close restaurants
    """


    def get(self, request):
        close_restaurants = self.get_queryset()
        return Response(close_restaurants)

    def get_queryset(self):
        """
        calculate the total , the average and the standard deviation of rating of restaurants that fall
        inside the circle with center and radius
        Returns
        -------
        dict
            a dictionary with statistics
        """

        lat = Decimal(self.request.query_params.get('latitude'))
        lng = Decimal(self.request.query_params.get('longitude'))
        radius = Decimal(self.request.query_params.get('radius'))
        point = GEOSGeometry("POINT({0} {1})".format(lng, lat))
        close_restaurants = Restaurant.objects.filter(location__distance_lt=(point, Distance(m=radius)))

        ratings = np.array([i.rating for i in close_restaurants])

        std = np.std(ratings)
        avg = np.mean(ratings)
        count = len(ratings)

        return {
            "data": {
                "count": count,
                "avg": avg,
                "std": std
            }
        }

