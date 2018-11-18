from django.urls import path
from .views import home, login_home
from .views import edit_terminal, remove_terminal, activate_terminal, add_item
from .views import remove_item, logout_view, start, add_item_size, user_home, user_order
from .views import main, about_us, how_it_works, setup_success, edit_menu, remove_menu, activate_menu
from django.contrib.auth.views import login

urlpatterns = [
    path('', main),
    path('user', user_home),
    path('user/order', user_order),
    path('start', start),
    path('about-us', about_us),
    path('how-it-works', how_it_works),
    path('register', home),
    path('login', login, {'template_name': 'login-cafe.html'}),
    path('home/', login_home),
    path('home/success', setup_success),
    path('home/edit-menu', edit_menu),
    path('home/edit-menu/remove-menu/<menu_id>', remove_menu),
    path('home/edit-menu/activate-menu/<mid>', activate_menu),
    path('home/edit-terminal', edit_terminal),
    path('home/edit-terminal/remove-terminal/<terminal_id>', remove_terminal),
    path('home/edit-terminal/activate-terminal/<tid>', activate_terminal),
    path('home/edit-item', add_item),
    path('home/edit-item/add-size/<item_id>', add_item_size),
    path('home/edit-item/remove-item/<item_id>', remove_item),
    path('home/logout', logout_view)
]
