from django.shortcuts import render
from manager.models import Restaurant
from .models import Runner
from django.http import HttpResponseRedirect


def home(request):
    error = False
    if request.method == 'POST':
        res_id = request.POST['select-res']
        runner_id = request.POST['runner_id']
        res = Restaurant.objects.get(id=res_id)
        runners = Runner.objects.filter(restaurant=res)
        if runners.filter(runner_id=runner_id).exists():
            runner = runners.get(runner_id=runner_id)
            # return render(request, 'home_chef.html', {'chef': chef})
            return HttpResponseRedirect('home/' + runner.runner_id + "/" + res_id)
        else:
            error = True
    return render(request, 'login_runner.html', {'restaurants': Restaurant.objects.all(), 'error': error})


def main(request, run_id, run_res):
    runner = Runner.objects.filter(restaurant=run_res).get(runner_id=run_id)
    return render(request, 'home_runner.html', {'runner': runner})
