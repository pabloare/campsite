from django.urls import path
from .views import home, main
from .orders import render_orders, dish_complete, ready, dish_complete_autoserve

urlpatterns = [
    path('', home),
    path('home/<chef_id>/<str:chef_res>', main),
    path('ready/<res_id>/<chef_id>/<order_id>', ready),
    path('home/update/<chef_id>/<res_id>', render_orders),
    path('home/<str:join_id>', dish_complete),
    path('home/autoserve/<order_id>/<chef_id>', dish_complete_autoserve),
]
