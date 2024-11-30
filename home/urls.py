from django.urls import path
from home.views import home

urlpatterns = [

    path('', home, name='home'),
    # path('course/detail/<int:pk>/', product_detail, name='product-detail'),
    # path('category/<int:pk>/products', category_products, name='category-products'),
    # path('category/<int:pk>/detail', category_detail, name='category-detail'),
]