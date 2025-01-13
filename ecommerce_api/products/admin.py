from django.contrib import admin
from .models import Category, Product, Wishlist, Review

"""admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Review)"""

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock_quantity', 'created_date')
    search_fields = ['name', 'category__name']
    list_filter = ('category',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'added_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating', 'created_date')
    list_filter = ('product', 'rating')

