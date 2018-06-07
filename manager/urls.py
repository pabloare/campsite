from django.urls import path
from .views import home, login_home
from django.contrib.auth.views import login

urlpatterns = [
    path('', home),
    path('login', login, {'template_name': 'login.html'}),
    path('home/', login_home)
]
