from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Chef, Join
from manager.models import Restaurant, Dish


def home(request):
    error = False
    if request.method == 'POST':
        res_id = request.POST['select-res']
        chef_id = request.POST['chef_id']
        res = Restaurant.objects.get(id=res_id)
        chefs = Chef.objects.filter(restaurant=res)
        if chefs.filter(chef_id=chef_id).exists():
            chef = chefs.get(chef_id=chef_id)
            # return render(request, 'home_chef.html', {'chef': chef})
            return HttpResponseRedirect('home/' + chef.chef_id + "/" + res_id)
        else:
            error = True
    return render(request, 'login_chef.html', {'restaurants': Restaurant.objects.all(), 'error': error})


def main(request, chef_id, chef_res):
    chef = Chef.objects.filter(restaurant=chef_res).get(chef_id=chef_id)
    return render(request, 'home_chef.html', {'chef': chef})
