from django.urls import path
from .views import home, ordering, pay

urlpatterns = [
    path('', home),
    path('order/<username>/<seat>/<table>/<restaurant>', ordering),
    path('pay/<username>/<res_name>/<table_num>/<seat_num>', pay),
]
