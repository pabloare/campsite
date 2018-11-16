from django.contrib import admin
from django.urls import path, include
from user.views import initial_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('manager.urls')),
    path('cafe/', include("cafe.urls")),
    path('chef/', include('chef.urls')),
    path('runner/', include('runner.urls')),
    path('', initial_view),
    path('user/', include('user.urls')),
]
