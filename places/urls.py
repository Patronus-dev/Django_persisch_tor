from django.urls import path
from .views import *

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('place/<int:pk>/', PlaceDetailView.as_view(), name='place_detail'),
]
