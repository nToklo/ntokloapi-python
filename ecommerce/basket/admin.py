from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, {
            'fields': ('user', 'quantity', 'status', 'products')
        }
        ),
    )
    list_display = ('user', 'pub_date', 'quantity', 'status')
