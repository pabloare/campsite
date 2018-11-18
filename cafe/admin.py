from django.contrib import admin
from .models import Cafe, Owner, Terminal, Item, Size

# Register your models here.
admin.site.register(Item)
admin.site.register(Terminal)
admin.site.register(Owner)
admin.site.register(Cafe)
admin.site.register(Size)
