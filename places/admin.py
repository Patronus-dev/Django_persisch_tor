from django.contrib import admin
from .models import Place


@admin.register(Place)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'city', 'datetime_created', 'id', )
    ordering = ('category', )
