from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import stripe
from campsite import settings
import requests
from .models import Cafe, Owner, Terminal, Item, Menu, Size

stripe.api_key = settings.STRIPE_SECRET_KEY


def main(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/cafe/home')
    return render(request, 'main-cafe.html')


def start(request):
    return render(request, 'start.html')


def about_us(request):
    # Render about us page
    return render(request, 'about_us.html')


def how_it_works(request):
    # Render How it works page
    return render(request, 'how_it_works.html')


def setup_success(request):
    try:
        account_code = request.GET['code']
    except:
        return render('login_home-cafe.html', {'error': True})
    account = {'client_secret': stripe.api_key, 'code': account_code, 'grant_type': 'authorization_code'}
    content = requests.post('https://connect.stripe.com/oauth/token', params=account)
    content_in_json = content.json()
    stripe_id = content_in_json['stripe_user_id']
    cafe = request.user.owner.cafe
    cafe.stripe_id = stripe_id
    cafe.save()
    return render(request, 'login_home.html', {'success': True})


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        u = User.objects.create(username=username)
        email = request.POST['email']
        password = request.POST['password']
        u.set_password(password)
        u.save()
        cafe = request.POST['cafe']
        cafe_object = Cafe(name=cafe)
        cafe_object.save()
        new_owner = Owner(user=u, email=email, cafe=cafe_object)
        new_owner.save()
        return HttpResponseRedirect('/cafe/login')
    return render(request, 'home-cafe.html')


@login_required()
def login_home(request):
    return render(request, 'login_home-cafe.html', {'selector': 0})


@login_required()
def edit_terminal(request):
    if request.method == 'POST':
        cafe = request.user.owner.cafe
        name = request.POST['name']
        terminals = Terminal.objects.filter(cafe=cafe)
        if terminals.filter(name=name).exists():
            return render(request, 'edit_chef.html', {'error': True})
        terminal = Terminal(name=name, cafe=cafe, active=False)
        terminal.save()
        return HttpResponseRedirect('/cafe/home/edit-terminal')
    return render(request, 'edit_terminal.html', {'error': False})


@login_required()
def edit_menu(request):
    if request.method == 'POST':
        cafe = request.user.owner.cafe
        name = request.POST['name']
        description = request.POST['description']
        menus = Menu.objects.filter(cafe=cafe)
        if menus.filter(name=name).exists():
            return render(request, 'edit_menu.html', {'error': True})
        menu = Menu(name=name, cafe=cafe, description=description, active=False)
        menu.save()
        return HttpResponseRedirect('/cafe/home/edit-menu')
    return render(request, 'edit_menu.html', {'error': False})


@login_required()
def activate_menu(request, mid):
    cafe = request.user.owner.cafe
    menu = Menu.objects.get(id=mid, cafe=cafe)
    if menu.active:
        menu.active = False
        menu.save()
    elif not menu.active:
        menu.active = True
        menu.save()
    return HttpResponseRedirect('/cafe/home/edit-menu')


@login_required()
def remove_menu(request, menu_id):
    cafe = request.user.owner.cafe
    menu = Menu.objects.get(id=menu_id, cafe=cafe)
    menu.delete()
    return HttpResponseRedirect('/cafe/home/edit-menu')


@login_required()
def remove_terminal(request, terminal_id):
    cafe = request.user.owner.cafe
    terminal = Terminal.objects.get(id=terminal_id, cafe=cafe)
    terminal.delete()
    return HttpResponseRedirect('/cafe/home/edit-terminal')


@login_required()
def activate_terminal(request, tid):
    cafe = request.user.owner.cafe
    terminal = Terminal.objects.get(id=tid, cafe=cafe)
    if terminal.active:
        terminal.active = False
        terminal.save()
    elif not terminal.active:
        terminal.active = True
        terminal.save()
    return HttpResponseRedirect('/cafe/home/edit-terminal')


@login_required()
def add_item(request):
    if request.method == 'POST':
        cafe = request.user.owner.cafe
        name = request.POST['name']
        menu_id = request.POST['select-menu']
        try:
            menu = Menu.objects.get(id=menu_id)
        except:
            return render(request, 'edit_item.html', {'error': True})
        items = Item.objects.filter(cafe=cafe)
        if items.filter(name=name).exists():
            return render(request, 'edit_item.html', {'error': True})
        desc = request.POST['desc']
        time = request.POST['time']
        price = request.POST['price']
        item = Item(cafe=cafe, name=name, description=desc, time_to_do=time, price=price, menu=menu)
        item.save()
        return HttpResponseRedirect('/cafe/home/edit-item')
    return render(request, 'edit_item.html', {'error': False})


@login_required()
def add_item_size(request, item_id):
    if request.method == 'POST':
        name = request.POST['name']
        item = Item.objects.get(id=item_id)
        size = Size(name=name, item=item)
        size.save()
        return HttpResponseRedirect('/cafe/home/edit-item')
    return render(request, 'edit_item.html')


@login_required()
def remove_item(request, item_id):
    cafe = request.user.owner.cafe
    item = Item.objects.filter(cafe=cafe).get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/cafe/home/edit-item')


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cafe/login')
