from django.contrib import admin

from .models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Country)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'status', 'location', 'beds', 'baths', 'floors', 'metro', 'area', 'size',
                    'address', 'city', 'country')
