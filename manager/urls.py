from django.urls import path
from .views import home, login_home, edit_tables, remove_seat, add_seat, add_table
from django.contrib.auth.views import login

urlpatterns = [
    path('', home),
    path('login', login, {'template_name': 'login.html'}),
    path('home/', login_home),
    path('home/edit-tables', edit_tables),
    path('home/edit-tables/remove-seat/<table>', remove_seat),
    path('home/edit-tables/add-seat/<table>/<int:count>', add_seat),
    path('home/add-table/<int:restaurant_id>', add_table)

]
