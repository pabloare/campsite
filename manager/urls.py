from django.urls import path
from .views import home
from django.contrib.auth.views import login

urlpatterns = [
    path('', home),
    path('login', login, {'template_name': 'login.html'})
]
