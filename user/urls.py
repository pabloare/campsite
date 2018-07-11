from django.urls import path
from .views import home, ordering

urlpatterns = [
    path('', home),
    path('order/<username>/<seat>/<table>/<restaurant>', ordering),
]
