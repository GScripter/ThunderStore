from django.contrib import admin
from . models import Category, Product, ProductImage, Assessment

# Register your models here.
admin.site.register(Category)
class ImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class AssessmentInline(admin.TabularInline):
    model = Assessment
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['id']
    inlines = [ImagesInline, AssessmentInline]

