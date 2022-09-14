from django.contrib import admin
from .models import *


class BalloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'photo', 'is_onsite')
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'group')
    list_editable = ('is_onsite',)
    list_filter = ('time_create', 'is_onsite',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Group, GroupAdmin)
