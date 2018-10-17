from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Manager, Restaurant, Table, Seat, Dish
from chef.models import Chef
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from runner.models import Runner


def main(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/home')
    return render(request, 'main.html')


def start(request):
    return render(request, 'start.html')


def about_us(request):
    # Render about us page
    return render(request, 'about_us.html')


def how_it_works(request):
    # Render How it works page
    return render(request, 'how_it_works.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        u = User.objects.create(username=username)
        email = request.POST['email']
        password = request.POST['password']
        u.set_password(password)
        u.save()
        restaurant = request.POST['restaurant']
        operation = request.POST['select-autoserve']
        autoserve = False
        if operation == "autoserve":
            autoserve = True
        res = Restaurant(name=restaurant, autoserve=autoserve)
        res.save()
        new_manager = Manager(user=u, email=email, restaurant=res)
        new_manager.save()
        return HttpResponseRedirect('/manager/login')
    return render(request, 'home.html')


@login_required()
def login_home(request):
    return render(request, 'login_home.html', {'selector': 0})


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
def add_seat(request, table):
    # There might be an error of asynchronous commands and same seat
    table_object = Table.objects.get(pk=table)
    new_count = table_object.seat.all().count() + 1
    seat_object = Seat(table=table_object, seat_number=new_count, payed=True)
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
def edit_runner(request):
    if request.method == 'POST':
        restaurant = request.user.manager.restaurant
        runner_id = request.POST['runner_id']
        runners = Runner.objects.filter(restaurant=restaurant)
        if runners.filter(runner_id=runner_id).exists():
            return render(request, 'edit_runner.html', {'error': True})
        runner = Runner(restaurant=restaurant, runner_id=runner_id, active=False)
        runner.save()
        return HttpResponseRedirect('/manager/home/edit-runner')
    return render(request, 'edit_runner.html', {'error': False})


@login_required()
def remove_chef(request, chef_id):
    restaurant = request.user.manager.restaurant
    chef = Chef.objects.get(chef_id=chef_id, restaurant=restaurant)
    chef.delete()
    return HttpResponseRedirect('/manager/home/edit-chef')


@login_required()
def remove_runner(request, runner_id):
    restaurant = request.user.manager.restaurant
    runner = Runner.objects.get(runner_id=runner_id, restaurant=restaurant)
    runner.delete()
    return HttpResponseRedirect('/manager/home/edit-runner')


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
def activate_runner(request, rid):
    restaurant = request.user.manager.restaurant
    runner = Runner.objects.get(runner_id=rid, restaurant=restaurant)
    if runner.active:
        runner.active = False
        runner.save()
    elif not runner.active:
        runner.active = True
        runner.save()
    return HttpResponseRedirect('/manager/home/edit-runner')


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
        time = request.POST['time']
        price = request.POST['price']
        dish = Dish(restaurant=rest, dish_number=dish_n, description=desc, name=d_name, time_to_do=time, price=price)
        dish.save()
        return HttpResponseRedirect('/manager/home/edit-dish')
    return render(request, 'edit_dish.html', {'error': False})


@login_required()
def remove_dish(request, dish_num):
    res = request.user.manager.restaurant
    dish = Dish.objects.filter(restaurant=res).get(dish_number=dish_num)
    dish.delete()
    return HttpResponseRedirect('/manager/home/edit-dish')


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/manager/login')
