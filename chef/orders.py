from django.shortcuts import render
from .models import Chef, Join
from manager.models import Dish, Restaurant
from django.http import HttpResponseRedirect


def render_orders(request, chef_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    chef = Chef.objects.filter(restaurant=res).get(chef_id=chef_id)
    # Testing
    # dish = Dish.objects.get(name="California Roll")
    # add_order = Join(chef=chef, dish=dish)
    # add_order.save()
    joins = Join.objects.filter(chef=chef)
    return render(request, 'chef-orders.html', {'chef': chef, 'res': res_id, 'joins': joins})


def dish_complete(request, join_id):
    join = Join.objects.get(id=join_id)
    join.chef.accumulator -= join.dish.time_to_do
    chef_id = str(join.chef.chef_id)
    res_id = str(join.chef.restaurant.id)
    join.chef.save()
    join.delete()
    return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
