from django.shortcuts import render, redirect
from django.views.generic import *

from places.models import Place


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # دریافت مقادیر منحصربه‌فرد از دسته‌بندی‌ها
        context['places'] = Place.objects.all().distinct('category')
        return context
