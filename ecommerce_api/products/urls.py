from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ReviewList

router = DefaultRouter(trailing_slash=False)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_pk>/reviews/', ReviewList.as_view(), name='review-list'),
]

