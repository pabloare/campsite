from django.urls import path
from .views import home, main, render_orders

urlpatterns = [
    path('', home),
    path('home/<chef_id>/<str:chef_res>', main),
    path('home/update', render_orders)
]
