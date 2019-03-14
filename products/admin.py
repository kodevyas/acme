from django.contrib import admin

# Register your models here.
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'active')
    list_editable = ('active', )
    list_filter = ('active', )
    search_fields = ('sku', 'name')
