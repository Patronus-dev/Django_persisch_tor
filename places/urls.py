from django.urls import path
from .views import *

urlpatterns = [
    path('', PlaceListView.as_view(), name='place_list'),
    path('place/<int:pk>/', place_detail_view, name='place_detail'),
    path('create/', CreatePlaceView.as_view(), name='place_create'),
    path('related_services/', user_search_place_view, name='user_search'),
]
