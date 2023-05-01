from django.contrib import admin

from phones.models import Phone

# Register your models here.

# admin.site.register(Phone)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date', 'lte_exists', 'image']
    list_filter = ['name', 'price']