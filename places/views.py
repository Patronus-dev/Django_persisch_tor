from django.shortcuts import render
from django.views.generic import *

from .models import Place


class PlaceListView(ListView):
    model = Place
    paginate_by = 20
    template_name = 'places/place_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        queryset = super().get_queryset()

        # دریافت پارامتر کتگوری از URL
        category = self.request.GET.get('category')

        if category:
            # فیلتر کردن بر اساس کتگوری
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # دریافت دسته‌بندی‌های یکتا که حداقل یک مکان دارند
        categories_with_places = Place.objects.values_list('category', flat=True).distinct()
        context['categories'] = categories_with_places

        return context


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_detail.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # گرفتن لیست تصاویر
        images = [
            self.object.image2,
            self.object.image3,
            self.object.image4,
            self.object.image5
        ]

        # حذف تصاویر خالی (None)
        valid_images = [img.url for img in images if img]

        # ارسال لیست تصاویر به قالب
        context['images'] = valid_images

        return context
