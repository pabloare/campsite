from django.urls import path
from .views import home, main
from .orders import render_orders, dish_complete

urlpatterns = [
    path('', home),
    path('home/<chef_id>/<str:chef_res>', main),
    path('home/update/<chef_id>/<res_id>', render_orders),
    path('home/<chef_id>/<dish_num>/<res_id>', dish_complete)
]
