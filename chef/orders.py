from django.shortcuts import render
from .models import Chef, Join
from manager.models import Restaurant
from django.http import HttpResponseRedirect


def render_orders(request, chef_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    chef = Chef.objects.filter(restaurant=res).get(chef_id=chef_id)
    joins = Join.objects.filter(chef=chef, ready=False).order_by('created_at')
    return render(request, 'chef-orders.html', {'chef': chef, 'res': res_id, 'joins': joins})


def dish_complete(request, join_id):
    join = Join.objects.get(id=join_id)
    join.chef.accumulator -= join.dish.time_to_do
    chef_id = str(join.chef.chef_id)
    res_id = str(join.chef.restaurant.id)
    join.chef.save()
    join.ready = True
    join.save()
    return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
