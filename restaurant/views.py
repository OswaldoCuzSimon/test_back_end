from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant


class RestaurantView(APIView):
    def get(self, request):
        articles = Restaurant.objects.all()
        return Response({"restaurants": articles})