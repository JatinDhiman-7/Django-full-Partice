from django.urls import path
from . import views
urlpatterns=[
path('',views.Home,name='shop-home'),
path('products/',views.products,name='shop-products'),
]