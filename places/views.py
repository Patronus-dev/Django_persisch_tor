from django.shortcuts import render
from django.views.generic import *

from .models import Place


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'
    context_object_name = 'place'
