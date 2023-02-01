from django.contrib import admin
from .models import *


@admin.register(Balloon)
class BalloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'photo', 'is_onsite')
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'group')
    list_editable = ('is_onsite',)
    list_filter = ('time_create', 'is_onsite',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 8


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name__istartswith',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'photo', 'created_on')
    list_display_links = ('name',)
    search_fields = ('name__istartswith',)
