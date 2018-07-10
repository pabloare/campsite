from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        restaurant = request.POST['restaurant']
        table = request.POST['table']
        seat_num = request.POST['seat_num']
        restaurant = Restaurant.objects.get(name=restaurant)
        table = Table.objects.get(restaurant=restaurant, table_num=table)
        seat = Seat.objects.get(table=table, seat_number=seat_num)
        # if someone is in the seat or has not payed do not release seat
        if not seat.payed:
            pass
            # Throw error about how seat is occupied (use HttpResponseRedirect)
        # Create order to link dishes to
        username = request.POST['username']
        # lock seat when user has entered seat
        seat.payed = False
        order = Order(username=username, seat=seat, note='')
        # render new page where order is displayed with the order passed on
    # render normal view


def ordering(request, username, seat, table, restaurant):
    # If user is trying to add to order
    restaurant = Restaurant.objects.get(name=restaurant)
    table = Table.objects.get(restaurant=restaurant, table_num=table)
    seat = Seat.objects.get(table=table, seat_number=seat_num)
    order = Order.object.get(username=username, seat=seat)
    if request.method == 'POST':
        num_items = request.POST['num_items']
        item = request.POST['item']
        for i in range(num_items):
            order_dishes(restaurant, item, order)
    ordered_dishes = order.dishes.all()
    # render ordered dishes to view


def order_dishes(restaurant, item, order):
    dish = Dishes.objects.get(restaurant=restaurant, name=item)
    add_to = JoinOrder(dish=dish, order=order)
    add_to.save()
    send_to_chef(dish, restaurant)


def send_to_chef(dish):
    chefs = Chef.objects.filter(restaurant=restaurant)
    # TODO: make sure at least on chef is active
    chef_chosen = chefs.first()
    for chef in chefs:
        if chef.active:
            if chef.accumulator < chef_chosen.accumulator:
                chef_chosen = chef
    add_order = Join(chef=chef_chosen, dish=dish)
    add_order.save()
    # TODO: add the field time to each dish to see how long it takes and update accumulator
    chef_chosen.accumulator += dish.time
    
