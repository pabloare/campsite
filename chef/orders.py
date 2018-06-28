from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Chef
from manager.models import Restaurant, Dish


def render_orders(request, chef_id, res_name):
    dishes = Dish.objects.all()
    return render(request, 'chef-orders.html', {'dishes': dishes})
