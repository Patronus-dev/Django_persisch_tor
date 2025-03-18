from django.shortcuts import render
from django.views.generic import *
from django.shortcuts import get_object_or_404

from .models import Place
from .forms import CommentForm


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


# class PlaceDetailView(DetailView):
#     model = Place
#     template_name = 'places/place_detail.html'
#     context_object_name = 'place'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # گرفتن لیست تصاویر
#         images = [
#             self.object.image2,
#             self.object.image3,
#             self.object.image4,
#             self.object.image5
#         ]
#
#         # حذف تصاویر خالی (None)
#         valid_images = [img.url for img in images if img]
#
#         # ارسال لیست تصاویر به قالب
#         context['images'] = valid_images
#
#         return context
#
#
# def place_detail_view(request, pk):
#     place = get_object_or_404(Place, pk=pk)
#     place_comments = place.comments.all()
#
#     return render(request, 'places/place_detail.html', {'place': place, 'comments': place_comments})

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
        print('سلااااااااااااااااااااااااام')

    return render(request, 'places/place_detail.html', {'place': place,
                                                        'comments': place_comments,
                                                        'images': images,
                                                        'comment_form': comment_form,
                                                        })
