from django.contrib import admin
from .models import Dish, Manager, Restaurant, Seat, Table

admin.site.register(Dish)
admin.site.register(Manager)
admin.site.register(Restaurant)
admin.site.register(Seat)
admin.site.register(Table)
