from django.shortcuts import render
from manager.models import Seat, Restaurant, Table, Dish
from .models import Order, JoinOrder
from chef.models import Chef, Join
from django.http import HttpResponseRedirect


def home(request):
    error = False
    if request.method == 'POST':
        restaurant = request.POST['select-res']
        table = request.POST['table']
        seat_num = request.POST['seat_num']
        restaurant_object = Restaurant.objects.get(id=restaurant)
        table_object = Table.objects.get(restaurant=restaurant_object, table_number=table)
        seat = Seat.objects.get(table=table_object, seat_number=seat_num)
        # if someone is in the seat or has not payed do not release seat
        if not seat.payed:
            error = True
            return render(request, 'user_home.html', {'error': error, 'restaurants': Restaurant.objects.all()})
            # Throw error about how seat is occupied (use HttpResponseRedirect)
        # Create order to link dishes to
        username = request.POST['username']
        # lock seat when user has entered seat
        seat.payed = False
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
        for i in range(int(num_items)):
            order_dishes(restaurant, item, order)
    ordered_dishes = order.dishes.all()
    return render(request, 'ordering.html', {'username': username, 'ordered_dishes': ordered_dishes})
    # render ordered dishes to view along with username so we can later delete the join order
    #


def order_dishes(restaurant, item, order):
    dish = Dish.objects.get(restaurant=restaurant, name=item)
    add_to = JoinOrder(dish=dish, order=order)
    add_to.save()
    send_to_chef(dish, restaurant)


def send_to_chef(dish, restaurant):
    chefs = Chef.objects.filter(restaurant=restaurant)
    # TODO: make sure at least one chef is active
    chef_chosen = chefs.first()
    for chef in chefs:
        if chef.active:
            if chef.accumulator < chef_chosen.accumulator:
                chef_chosen = chef
    add_order = Join(chef=chef_chosen, dish=dish)
    add_order.save()
    chef_chosen.accumulator += dish.time_to_do
    chef_chosen.save()
