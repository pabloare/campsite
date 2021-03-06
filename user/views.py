from django.shortcuts import render
from manager.models import Seat, Restaurant, Table, Dish
from .models import Order, JoinOrder, Payment
from chef.models import Chef, Join
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import stripe
from campsite import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def initial_view(request):
    return HttpResponseRedirect('cafe/user')


def home(request):
    error = False
    if request.method == 'POST':
        restaurant = request.POST['select-res']
        table = request.POST['table']
        seat_num = request.POST['seat_num']
        restaurant_object = Restaurant.objects.get(id=restaurant)
        # TODO: Check the table exists and seat exists
        if not Table.objects.filter(restaurant=restaurant_object, table_number=table).exists():
            error = "Table"
            return render(request, 'user_home.html', {'error': error, 'restaurants': Restaurant.objects.all()})
        table_object = Table.objects.get(restaurant=restaurant_object, table_number=table)
        seat = Seat.objects.get(table=table_object, seat_number=seat_num)
        # if someone is in the seat or has not payed do not release seat
        if not seat.payed:
            error = "Seat"
            return render(request, 'user_home.html', {'error': error, 'restaurants': Restaurant.objects.all(), 'seat': seat})
        # Create order to link dishes to
        username = request.POST['username']
        # lock seat when user has entered seat
        seat.payed = False
        seat.save()
        payment = Payment()
        payment.save()
        order = Order(username=username, seat=seat, note='', payment=payment, restaurant=restaurant_object)
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
        if not note:
            note = ""
        for i in range(int(num_items)):
            # passed note as parameter
            order_dishes(restaurant, item, order, note)
    ordered_dishes = order.dishes.all()
    all_dishes = Dish.objects.filter(restaurant=restaurant).all()
    # See if chef has finished all dishes (i.e, deleted all joins) in order to make the user payment available
    return render(request, 'ordering.html', {'username': username, 'ordered_dishes': ordered_dishes, 'res_name': restaurant.name, 'table_num': table.table_number, 'seat_num': seat.seat_number, 'order': order, 'has_payed': False, 'all_dishes': all_dishes})
    # render ordered dishes to view along with username so we can later delete the join order


# Added note parameter for note in join
def order_dishes(restaurant, item, order, note):
    dish = Dish.objects.get(restaurant=restaurant, name=item)
    add_to = JoinOrder(dishes=dish, order=order)
    add_to.save()
    order.total += dish.price
    order.save()
    # passed note as parameter
    if not restaurant.autoserve:
        send_to_chef(dish, restaurant, order, note)


# Added note parameter for note in join
def send_to_chef(dish, restaurant, order, note):
    chefs = Chef.objects.filter(restaurant=restaurant)
    for chef in chefs:
        if chef.active:
            chef_chosen = chef
            break
    for chef in chefs:
        if chef.active:
            if chef.accumulator < chef_chosen.accumulator:
                chef_chosen = chef
    # create join with note and not ready
    add_order = Join(restaurant=restaurant, chef=chef_chosen, dish=dish, order=order, note=note, ready=False)
    add_order.save()
    chef_chosen.accumulator += dish.time_to_do
    chef_chosen.save()


# This will not work until I add the server and he clicks on the dish
# and the join is actually deleted after he clicks on it (before the join is only ready)
# When user pays: Clear all dishes ordered (Joint objects). Delete order and make seat available
def pay(request, username, res_name, table_num, seat_num):
    restaurant = Restaurant.objects.get(name=res_name)
    table = Table.objects.get(restaurant=restaurant, table_number=table_num)
    seat = Seat.objects.get(table=table, seat_number=seat_num)
    order = Order.objects.get(username=username, seat=seat)
    joins = Join.objects.filter(order=order)
    if request.method == "POST":
        if not restaurant.autoserve:
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(amount=int(order.total * 100), currency='cad', description='Charge', source=token, stripe_account=restaurant.stripe_id)
            order.save()
        elif restaurant.autoserve:
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(amount=int(order.total * 100), currency='cad', description='Charge', source=token, stripe_account=restaurant.stripe_id)
            order.payment.wants_to_pay = True
            order.payment.save()
            order.save()
        return HttpResponseRedirect('/user/pay/confirmation' + '/' + str(order.id))
    return HttpResponseRedirect('/user/')


def confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'payment_confirmation.html', {'order': order})


def pay_exit(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        allow_exit = False
        if order.payment.has_payed:
            allow_exit = True
            order.dishes.clear()
            order.seat.payed = True
            order.seat.save()
            order.payment.delete()
            order.delete()
            allow_exit = True
    except ObjectDoesNotExist:
        allow_exit = True
    return render(request, 'exit_confirmation.html', {'allow_exit': allow_exit})


def no_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.seat.payed = True
    order.seat.save()
    order.payment.delete()
    order.delete()
    return HttpResponseRedirect('/user/')
