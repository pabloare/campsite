from django.urls import path
from .views import home, main

urlpatterns = [
    path('', home),
    path('home/<chef_id>/<str:chef_res>', main),
]
