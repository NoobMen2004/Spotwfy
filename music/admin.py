from django.contrib import admin

from .models import *


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['user', 'cat']
    search_fields = ['title']
    exclude = ['image']
    ordering = ['create_add', 'update_add']

admin.site.register(Category)
admin.site.register(PlayList)

