from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    def thumbnail(self , object):
        return format_html(f'<img src="{object.main_img.url}" width="200" style="border-radius: 10px" />')


    thumbnail.short_description = 'Product Picture'

    list_display = ('thumbnail' , 'title')


admin.site.register(Product,ProductAdmin)