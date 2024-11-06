from django.urls import path
from training.views import course_list,course_detail

urlpatterns = [

    path('', course_list, name='course-list'),
    path('/detail/<int:pk>', course_detail, name='course-detail'),
    # path('course/detail/<int:pk>/', product_detail, name='product-detail'),
    # path('category/<int:pk>/products', category_products, name='category-products'),
    # path('category/<int:pk>/detail', category_detail, name='category-detail'),
]