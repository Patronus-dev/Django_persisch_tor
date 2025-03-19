from django.contrib import admin
from .models import Place, Comment


@admin.register(Place)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'city', 'datetime_created', 'id', )
    ordering = ('category', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'user_rating', 'datetime_created', 'id', )
    ordering = ('datetime_created', )
