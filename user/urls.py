from django.urls import path
from .views import home, ordering, pay, confirmation, pay_exit, no_order

urlpatterns = [
    path('', home),
    path('order/<username>/<seat>/<table>/<restaurant>', ordering),
    path('pay/<username>/<res_name>/<table_num>/<seat_num>', pay),
    path('pay/confirmation/<order_id>', confirmation),
    path('pay/exit/<order_id>', pay_exit),
    path('no-order/<order_id>', no_order)
]
