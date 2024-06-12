from django.urls import path, include
from catalog.views import product_list, product_detail, home
from . import views

urlpatterns = [
    # URL pattern for the home view
    path('', home, name='home'),

    # URL patterns for the product views
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    
   
]
