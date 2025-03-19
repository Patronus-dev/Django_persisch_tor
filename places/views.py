from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *

from .models import Place
from .forms import CommentForm, PlaceFilterForm, NewPlaceForm


class PlaceListView(ListView):
    model = Place
    paginate_by = 18
    template_name = 'places/place_list.html'
    context_object_name = 'places'
    ordering = ['-datetime_created']

    def get_queryset(self):
        queryset = super().get_queryset()

        # فیلتر کردن فقط پست‌های منتشر شده
        queryset = queryset.filter(status='pub')  # فقط پست‌های منتشر شده را بیاور

        # دریافت پارامترهای فیلتر از فرم
        category = self.request.GET.get('category')
        city = self.request.GET.get('city')

        # فیلتر کردن بر اساس کتگوری و شهر (در صورت انتخاب)
        if category:
            queryset = queryset.filter(category=category)
        if city:
            queryset = queryset.filter(city=city)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # فرم فیلتر
        form = PlaceFilterForm(self.request.GET)

        # دریافت دسته‌بندی‌های یکتا
        unique_categories = Place.objects.values_list('category', flat=True).distinct()
        context['categories'] = unique_categories

        # دریافت شهرهای یکتا
        unique_cities = Place.objects.values_list('city', flat=True).distinct()
        context['cities'] = unique_cities

        # مقادیر انتخاب‌شده برای فیلتر
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_city'] = self.request.GET.get('city', '')
        context['form'] = form  # ارسال فرم به قالب

        return context


def place_detail_view(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place_comments = place.comments.all().order_by("datetime_created")

    # دریافت لیست تصاویر اضافی (فقط موارد غیر None)
    images = [img.url for img in [
        place.image2,
        place.image3,
        place.image4,
        place.image5
    ] if img]

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.place = place
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'places/place_detail.html', {'place': place,
                                                        'comments': place_comments,
                                                        'images': images,
                                                        'comment_form': comment_form,
                                                        })


def user_search_place_view(request):
    if request.method == "POST":
        user_search = request.POST['user_search']
        places = Place.objects.filter(title__icontains=user_search)
        return render(request, 'places/search_result.html', {'user_search': user_search, 'places': places})
    else:
        return render(request, 'places/search_result.html', {})


def place_list(request):
    places = Place.objects.all()

    city = request.GET.get('city')
    category = request.GET.get('category')

    if city:
        places = places.filter(city=city)

    if category:
        places = places.filter(category=category)

    categories = Place.objects.values_list('category', flat=True).distinct()
    cities = Place.objects.values_list('city', flat=True).distinct()

    return render(request, 'places/place_list.html', {
        'places': places,
        'categories': categories,
        'cities': cities,
        'selected_city': city,
        'selected_category': category
    })


class CreatePlaceView(CreateView):
    form_class = NewPlaceForm
    model = Place
    template_name = 'places/place_create.html'

