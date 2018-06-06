from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Manager, Restaurant
from django.http import HttpResponseRedirect


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
