from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Chef
from manager.models import Restaurant

# MAKE CUSTOM USER MODEL FOR CHEF WITH ONLY ID AND RESTAURANT FIELDS
def home(request):
    if request.method == 'POST':
        res_id = request.POST['select-res']
        chef_id = request.POST['chef_id']
        res = Restaurant.objects.get(id=res_id)
        chefs = Chef.objects.filter(restaurant=res)
        if chefs.filter(chef_id=chef_id).exists():

    return render(request, 'login_chef.html', {'restaurants': Restaurant.objects.all()})
