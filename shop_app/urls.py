from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cart/<int:id>', cart, name='cart'),
    path('shop/', shop, name='shop'),
    path('shipping/', shipping, name='shipping'),
    path('payment/', payment, name='payment'),
    path('order/', order, name='order'),
    path('thanks/', thanks, name='thanks'),
    path('my_account/', my_account, name='my_account'),
    path('my_orders/', my_orders, name='my_orders'),
    path('product/<int:id>', product, name='product'),
    path('register/', register, name='register'),
    # path('login/', login, name='login'),


]