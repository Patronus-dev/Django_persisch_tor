from django.urls import path
from .views import *

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('place/<int:pk>/', place_detail_view, name='place_detail'),
]
