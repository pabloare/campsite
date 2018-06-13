from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Manager, Restaurant, Table, Seat, Dish
from chef.models import Chef
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        u = User.objects.create(username=username)
        email = request.POST['email']
        password = request.POST['password']
        u.set_password(password)
        u.save()
        restaurant = request.POST['restaurant']
        res = Restaurant(name=restaurant)
        res.save()
        new_manager = Manager(user=u, email=email, restaurant=res)
        new_manager.save()
        return HttpResponseRedirect('login')
    return render(request, 'home.html')


@login_required()
def login_home(request):
    return render(request, 'login_home.html')


@login_required()
def edit_tables(request):
    return render(request, 'edit_tables.html')


@login_required()
def remove_seat(request, table):
    table_object = Table.objects.get(pk=table)
    seat = Seat.objects.filter(table=table_object).last()
    seat.delete()
    if Seat.objects.filter(table=table_object).count() == 0:
        for table in Table.objects.filter(restaurant=table_object.restaurant):
            if table.table_number > table_object.table_number:
                table.table_number = table.table_number - 1
                table.save()
        table_object.delete()
    return HttpResponseRedirect('/manager/home/edit-tables')


@login_required()
def add_seat(request, table, count):
    table_object = Table.objects.get(pk=table)
    new_count = count + 1
    seat_object = Seat(table=table_object, seat_number=new_count, payed=False)
    seat_object.save()
    return HttpResponseRedirect('/manager/home/edit-tables')


@login_required()
def add_table(request, restaurant_id):
    restaurant_object = Restaurant.objects.get(pk=restaurant_id)
    table_num = Table.objects.filter(restaurant=restaurant_object).count() + 1
    table = Table(restaurant=restaurant_object, table_number=table_num)
    table.save()
    return HttpResponseRedirect('/manager/home/edit-tables')


@login_required()
def edit_chef(request):
    if request.method == 'POST':
        restaurant = request.user.manager.restaurant
        chef_id = request.POST['chef_id']
        chefs = Chef.objects.filter(restaurant=restaurant)
        if chefs.filter(chef_id=chef_id).exists():
            return render(request, 'edit_chef.html', {'error': True})
        chef = Chef(chef_id=chef_id, restaurant=restaurant, accumulator=0, active=False)
        chef.save()
        return HttpResponseRedirect('/manager/home/edit-chef')
    return render(request, 'edit_chef.html', {'error': False})


@login_required()
def remove_chef(request, chef_id):
    restaurant = request.user.manager.restaurant
    chef = Chef.objects.get(chef_id=chef_id, restaurant=restaurant)
    chef.delete()
    return HttpResponseRedirect('/manager/home/edit-chef')


@login_required()
def activate_chef(request, cid):
    restaurant = request.user.manager.restaurant
    chef = Chef.objects.get(chef_id=cid, restaurant=restaurant)
    if chef.active:
        chef.active = False
        chef.save()
    elif not chef.active:
        chef.active = True
        chef.save()
    return HttpResponseRedirect('/manager/home/edit-chef')


@login_required()
def add_dish(request):
    if request.method == 'POST':
        rest = request.user.manager.restaurant
        dish_num = request.POST['dish_num']
        dish_n = int(dish_num)
        dishes = Dish.objects.filter(restaurant=rest)
        if dishes.filter(dish_number=dish_n).exists():
            return render(request, 'edit_dish.html', {'error': True})
        desc = request.POST['dish_desc']
        d_name = request.POST['dish_name']
        dish = Dish(restaurant=rest, dish_number=dish_n, description=desc, name=d_name)
        dish.save()
        return HttpResponseRedirect('/manager/home/edit-dish')
    return render(request, 'edit_dish.html', {'error': False})
