from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Chef
from manager.models import Restaurant


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
            return HttpResponseRedirect('feeds')
        else:
            error = True
    return render(request, 'login_chef.html', {'restaurants': Restaurant.objects.all(), 'error': error})
