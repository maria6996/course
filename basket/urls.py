from django.urls import path
from basket.views import add_to_basket,basket_list


urlpatterns = [
 path('add/', add_to_basket, name='add-to-basket'),
 path('list', basket_list, name='basket-list'),

]