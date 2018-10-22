from django.urls import path
from .views import home, ordering, pay, confirmation, pay_exit, test, test_success

urlpatterns = [
    path('', home),
    path('test', test),
    path('test/success', test_success),
    path('order/<username>/<seat>/<table>/<restaurant>', ordering),
    path('pay/<username>/<res_name>/<table_num>/<seat_num>', pay),
    path('pay/confirmation/<order_id>', confirmation),
    path('pay/exit/<order_id>', pay_exit)
]
