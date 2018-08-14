from django.urls import path
from .views import home, main
from .orders import render_orders, dish_complete

urlpatterns = [
    path('', home),
    path('home/<run_id>/<str:run_res>', main),
    path('home/update/<runner_id>/<res_id>', render_orders),
    path('home/<run_id>/<str:join_id>/<str:res_id>', dish_complete)
]
