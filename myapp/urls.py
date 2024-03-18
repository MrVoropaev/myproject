from django.urls import path
from .views import client_orders_list

urlpatterns = [
    path('client_orders/<int:client_id>/', client_orders_list, name='client_orders_list'),
]

