from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Car 
from django.utils.html import format_html
# Register your models here.

class Caradmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'Image'

    list_display = ('thumbnail','title','model','condition','is_feauterd')
    list_display_link = ('thumbnail','title')
    list_editable = ('is_feauterd',)
    search_fields = ('title','model')
    list_filter = ('condition',)

admin.site.register(Car,Caradmin)