from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Manager, Restaurant, Table, Seat
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
def remove_seat(request, seat):
    seat.delete()
    return render(request, 'edit_tables.html')


@login_required()
def add_seat(request, table, count):
    table_object = Table.objects.get(pk=table)
    new_count = count + 1
    seat_object = Seat(table=table_object, seat_number=new_count, payed=False)
    seat_object.save()
    return render(request, 'edit_tables.html')

# HAVE TODO DELETE DATABASE AND RESTART IT
@login_required()
def add_table(request, restaurant_id):
    restaurant_object = Restaurant.objects.get(pk=restaurant_id)
    table_num = Table.objects.count() + 1
    table = Table(restaurant=restaurant_object, table_number=table_num)
    table.save()
    return render(request, 'edit_tables.html')
