from django.contrib import admin
from . models import Category, Product, ProductImage

# Register your models here.
admin.site.register(Category)
class ImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

