from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RestaurantSerializer
from django.db.utils import IntegrityError
from .models import Restaurant


class RestaurantView(APIView):
    def get(self, request):
        articles = Restaurant.objects.all()
        serializer = RestaurantSerializer(articles, many=True)
        return Response({"restaurants": serializer.data})

    def post(self, request):
        try:
            article = request.data.get('restaurant')

            # Create an article from the above data
            serializer = RestaurantSerializer(data=article)
            if serializer.is_valid(raise_exception=True):
                restaurant_saved = serializer.save()
            serializer.validate_un
            return Response({
                "success": "Restaurant '{}' created successfully".format(restaurant_saved.name)
            }, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response([{"id": "id must be unique"}], status=status.HTTP_400_BAD_REQUEST)
