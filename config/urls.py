from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from language.views import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('places/', include('places.urls')),
    path('set-language/', set_language, name='set_language'),

    # Rosetta
    path('rosetta/', include('rosetta.urls')),
    # SEO
    path("django-check-seo/", include("django_check_seo.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
