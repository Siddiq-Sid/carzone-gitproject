from django.contrib import admin
from . models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image'

    list_display = ('car_title','thumbnail','color','car_model','is_featured')
    list_display_links = ('car_title','thumbnail')
    search_fields = ('color','car_model','is_featured')
    list_editable = ('is_featured',)
    list_filter = ('color','car_model','is_featured','fueltype')
admin.site.register(Car,CarAdmin)

