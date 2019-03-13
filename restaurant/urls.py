from django.urls import path

from .views import RestaurantView


app_name = "restaurant"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('restaurant/', RestaurantView.as_view()),
    path('restaurant/<uuid:restaurant_id>', RestaurantView.as_view())

]