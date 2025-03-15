from .models import Place


# برای ارسال categories به تمام صفحات با ایجاد یک context processor، می‌توانیم لیست دسته‌بندی‌ها را به تمام صفحات
# ارسال کنیم، بدون نیاز به تغییر در ویوهای مختلف.
def categories_context(request):
    categories = Place.objects.values_list('category', flat=True).distinct()
    return {'categories': categories}

# نکته !!!!! در بخش settings.py،در قسمت TEMPLATES فایل context_processors را ویرایش کنید:
# 'places.context_processors.categories_context',
