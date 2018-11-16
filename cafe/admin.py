from django.contrib import admin
from .models import Cafe, Owner, Terminal, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Terminal)
admin.site.register(Owner)
admin.site.register(Cafe)
