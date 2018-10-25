from django.shortcuts import render
from .models import Chef, Join
from manager.models import Restaurant
from django.http import HttpResponseRedirect
from user.models import Order


def render_orders(request, chef_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    chef = Chef.objects.filter(restaurant=res).get(chef_id=chef_id)
    joins = Join.objects.filter(chef=chef, ready=False).order_by('created_at')
    if res.autoserve:
        orders = Order.objects.filter(restaurant=res).order_by('updated_at')
        return render(request, 'chef-orders.html', {'chef': chef, 'res': res_id, 'orders': orders})
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


def dish_complete_autoserve(request, order_id, chef_id):
    order = Order.objects.get(id=order_id)
    order.payment.wants_to_pay = False
    order.payment.save()
    order.prepared = True
    order.save()
    return HttpResponseRedirect('/chef/home/' + str(chef_id) + "/" + str(order.restaurant.id))


def ready(request, res_id, chef_id, order_id):
    order = Order.objects.get(id=order_id)
    order.payment.has_payed = True
    order.payment.save()
    return HttpResponseRedirect('/chef/home/' + str(chef_id) + '/' + str(res_id))
