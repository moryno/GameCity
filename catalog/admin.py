from django.contrib import admin
from .models import Category, Product

# admin.site.register(Game)
# admin.site.register(Genre)
# admin.site.register(GameInstance)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price_in_shillings', 'stock', 'customer', 'available',
                    'created', 'updated')
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price_in_shillings', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}