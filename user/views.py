from django.shortcuts import render
from manager.models import Seat, Restaurant, Table, Dish
from .models import Order, JoinOrder
from chef.models import Chef, Join
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    error = False
    if request.method == 'POST':
        restaurant = request.POST['select-res']
        table = request.POST['table']
        seat_num = request.POST['seat_num']
        restaurant_object = Restaurant.objects.get(id=restaurant)
        # TODO: Check the table exists and seat exists
        table_object = Table.objects.get(restaurant=restaurant_object, table_number=table)
        seat = Seat.objects.get(table=table_object, seat_number=seat_num)
        # if someone is in the seat or has not payed do not release seat
        if not seat.payed:
            error = True
            return render(request, 'user_home.html', {'error': error, 'restaurants': Restaurant.objects.all(), 'seat': seat})
            # Throw error about how seat is occupied (use HttpResponseRedirect)
        # Create order to link dishes to
        username = request.POST['username']
        # lock seat when user has entered seat
        seat.payed = False
        seat.save()
        order = Order(username=username, seat=seat, note='')
        order.save()
        return HttpResponseRedirect('/user/order/' + username + '/' + seat_num + '/' + table + '/' + restaurant)
        # render new page where order is displayed with the order passed on
    # render normal view
    return render(request, 'user_home.html', {'error': error, 'restaurants': Restaurant.objects.all()})


def ordering(request, username, seat, table, restaurant):
    # If user is trying to add to order
    restaurant = Restaurant.objects.get(id=restaurant)
    table = Table.objects.get(restaurant=restaurant, table_number=table)
    seat = Seat.objects.get(table=table, seat_number=seat)
    order = Order.objects.get(username=username, seat=seat)
    if request.method == 'POST':
        num_items = request.POST['num_items']
        item = request.POST['item']
        note = request.POST['note']
        if note:
            order.note = note
            order.save()
        for i in range(int(num_items)):
            order_dishes(restaurant, item, order)
    ordered_dishes = order.dishes.all()
    # See if chef has finished all dishes (i.e, deleted all joins) in order to make the user payment available
    return render(request, 'ordering.html', {'username': username, 'ordered_dishes': ordered_dishes, 'res_name': restaurant.name, 'table_num': table.table_number, 'seat_num': seat.seat_number, 'order_id': order.id, 'has_payed': False})
    # render ordered dishes to view along with username so we can later delete the join order
    #


def order_dishes(restaurant, item, order):
    dish = Dish.objects.get(restaurant=restaurant, name=item)
    add_to = JoinOrder(dishes=dish, order=order)
    add_to.save()
    send_to_chef(dish, restaurant, order)


def send_to_chef(dish, restaurant, order):
    chefs = Chef.objects.filter(restaurant=restaurant)
    chef_chosen = chefs.first()
    for chef in chefs:
        if chef.active:
            if chef.accumulator < chef_chosen.accumulator:
                chef_chosen = chef
    add_order = Join(chef=chef_chosen, dish=dish, order=order)
    add_order.save()
    chef_chosen.accumulator += dish.time_to_do
    chef_chosen.save()


# When user pays: Clear all dishes ordered (Joint objects). Delete order and make seat available
def pay(request, username, res_name, table_num, seat_num):
    restaurant = Restaurant.objects.get(name=res_name)
    table = Table.objects.get(restaurant=restaurant, table_number=table_num)
    seat = Seat.objects.get(table=table, seat_number=seat_num)
    order = Order.objects.get(username=username, seat=seat)
    joins = Join.objects.filter(order=order)
    try:
        if not joins:
            order.dishes.clear()
            order.delete()
            seat.payed = True
            seat.save()
            return HttpResponseRedirect('/user/')
        else:
            return render(request, 'ordering.html', {'username': username, 'ordered_dishes': order.dishes.all(), 'res_name': restaurant.name, 'table_num': table.table_number, 'seat_num': seat.seat_number, 'order_id': order.id, 'has_payed': True})
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/user/')
