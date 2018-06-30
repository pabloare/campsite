from django.shortcuts import render
from .models import Chef, Join
from manager.models import Dish


def render_orders(request, chef_id, res_id):
    chef = Chef.objects.filter(restaurant=res_id).get(chef_id=chef_id)
    dish = Dish.objects.get(name="California Roll")
    add_order = Join(chef=chef, dish=dish)
    add_order.save()
    dishes = chef.dishes.all()
    return render(request, 'chef-orders.html', {'dishes': dishes, 'chef': chef.chef_id})
