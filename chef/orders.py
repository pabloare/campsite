from django.shortcuts import render
from .models import Chef, Join
from manager.models import Dish
from django.http import HttpResponseRedirect


def render_orders(request, chef_id, res_id):
    chef = Chef.objects.filter(restaurant=res_id).get(chef_id=chef_id)
    # dish = Dish.objects.get(name="California Roll")
    # add_order = Join(chef=chef, dish=dish)
    # add_order.save()
    dishes = chef.dishes.all()
    return render(request, 'chef-orders.html', {'dishes': dishes, 'chef': chef.chef_id, 'res': res_id})


def dish_complete(request, chef_id, dish_num, res_id):
    chef = Chef.objects.get(chef_id=chef_id)
    dish = Dish.objects.get(dish_number=dish_num)
    dishes = Join.objects.filter(chef=chef, dish=dish)
    try:
        completed_dish = dishes.get()
        completed_dish.delete()
        return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
    except:
        completed_dish = dishes.first()
        completed_dish.delete()
        return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
