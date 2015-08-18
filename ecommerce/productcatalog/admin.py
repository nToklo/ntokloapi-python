from django.contrib import admin
from productcatalog.models import Category, Manufacturer, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, {
            'fields': ('parent', 'slug', 'name', 'description')
            }
        ),
    )
    list_display = ('name', 'description', 'parent')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
            }
        ),
    )
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, {
            'fields': ('category', 'manufacturer', 'name', 'slug', 'description', 'photo',
                'price_in_sterling', 'available', 'instock')
            }
       ),
    )
    list_display = ('category', 'manufacturer', 'name', 'slug', 'description',
        'photo', 'price_in_sterling', 'available', 'instock')
    prepopulated_fields = {"slug": ("name",)}
