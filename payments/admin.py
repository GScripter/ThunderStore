from django.contrib import admin
from . models import Item, Order

# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_paid', 'is_sent']
    list_filter = ['is_sent', 'is_paid']
    search_fields = ['name']
    inlines = [ItemInline]
