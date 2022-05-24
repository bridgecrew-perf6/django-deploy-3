from django.contrib import admin
from .models import Gallery
from django.utils.html import format_html
# Register your models here.


class GalleryAdmin(admin.ModelAdmin):

    def thumbnail(self , object):
        return format_html(f'<img src="{object.img.url}" width="100" style="border-radius: 10px" />')


    thumbnail.short_description = 'Product Picture'

    list_display = ('thumbnail',)

admin.site.register(Gallery, GalleryAdmin)