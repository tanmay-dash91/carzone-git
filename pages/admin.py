from django.contrib import admin
from .models import Team
from django.utils.html import  format_html

# Register your models here.

class Teamadmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.photos.url))

    thumbnail.short_description = 'Image'
    list_display =('id','thumbnail','firstname','designation','created_date')
    list_display_links = ('id','thumbnail','firstname',)
    search_fields = ('firstname','designation')
    list_filter = ('designation',)

admin.site.register(Team,Teamadmin)


