from django.urls import path
from .views import ProductSingleView, CartView, ShopView, CartViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('', ShopView.as_view(), name='index'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
]

