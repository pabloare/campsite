from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', include('manager.urls')),
    path('chef/', include('chef.urls')),
    path('user/', include('user.urls')),
]
