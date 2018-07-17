from django.shortcuts import render
from .models import Chef, Join
from manager.models import Dish, Restaurant
from user.models import Order
from django.http import HttpResponseRedirect


def render_orders(request, chef_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    chef = Chef.objects.filter(restaurant=res).get(chef_id=chef_id)
    # Testing
    # dish = Dish.objects.get(name="California Roll")
    # add_order = Join(chef=chef, dish=dish)
    # add_order.save()
    order_seats = []
    order_tables = []
    dishes = chef.dishes.all()
    for dish in dishes:
        joins = Join.objects.filter(chef=chef, dish=dish)
        for join in joins:
            order = join.order
            order_seats.append(order.seat.seat_number)
            order_tables.append(order.seat.table.table_number)
    return render(request, 'chef-orders.html', {'dishes': dishes, 'chef': chef, 'res': res_id, 'order_seats': order_seats, 'order_tables': order_tables})


def dish_complete(request, chef_id, dish_num, res_id):
    res = Restaurant.objects.get(id=res_id)
    chef = Chef.objects.get(chef_id=chef_id, restaurant=res)
    dish_object = Dish.objects.get(restaurant=res, dish_number=dish_num)

    # Using without exceptions handling

    # dishes = Join.objects.filter(chef=chef, dish=dish)
    # try:
    #    completed_dish = dishes.get()
    #    completed_dish.delete()
    #    return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
    # except:
    #    completed_dish = dishes.first()
    #    completed_dish.delete()
    #    return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
    dish = Join.objects.filter(chef=chef, dish=dish_object).first()
    dish.delete()
    chef.accumulator -= dish_object.time_to_do
    chef.save()
    return HttpResponseRedirect('/chef/home/' + chef_id + "/" + res_id)
