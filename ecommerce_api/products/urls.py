"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import CategoryViewSet, ProductViewSet,WishlistViewSet, ReviewViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('wishlist', WishlistViewSet)

router.register('products', ProductViewSet)"""
"""
urlpatterns = router.urls 
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
urlpatterns = router.urls + products_router.urls"""

"""urlpatterns = [
      path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
   ]"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, WishlistViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'wishlist', WishlistViewSet)

# Nested review URL under product
product_router = DefaultRouter()
product_router.register(r'products/product/(?P<product_pk>\d+)/reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(product_router.urls)),
]

