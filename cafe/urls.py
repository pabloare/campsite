from django.urls import path
from .views import home, login_home
from .views import edit_terminal, remove_terminal, activate_terminal, add_item
from .views import remove_item, logout_view, start
from .views import main, about_us, how_it_works, setup_success
from django.contrib.auth.views import login

# TODO: Add menu functionality
urlpatterns = [
    path('', main),
    path('start', start),
    path('about-us', about_us),
    path('how-it-works', how_it_works),
    path('register', home),
    path('login', login, {'template_name': 'login.html'}),
    path('home/', login_home),
    path('home/success', setup_success),
    path('home/edit-terminal', edit_terminal),
    path('home/edit-terminal/remove-terminal/<terminal_id>', remove_terminal),
    path('home/edit-terminal/activate-terminal/<tid>', activate_terminal),
    path('home/edit-item', add_item),
    path('home/edit-item/remove-item/<item_id>', remove_item),
    path('home/logout', logout_view)
]
