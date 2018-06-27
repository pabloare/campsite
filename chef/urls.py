from django.urls import path
from .views import home
from .feed import OrderFeed

urlpatterns = [
    path('', home),
    path('feeds', OrderFeed()),

]
