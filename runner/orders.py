from django.shortcuts import render
from .models import Runner
from manager.models import Restaurant
from django.http import HttpResponseRedirect
from chef.models import Join


def render_orders(request, runner_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    runner = Runner.obejcts.filter(restaurant=res).get(runner_id=runner_id)
    # Testing
    # dish = Dish.objects.get(name="California Roll")
    # add_order = Join(chef=chef, dish=dish)
    # add_order.save()
    # only display dishes that have  been finished
    joins = Join.objects.filter(restaurant=res, ready=True)

    return render(request, 'chef-orders.html', {'runner': runner, 'res': res_id, 'joins': joins})


def dish_complete(request, run_id, join_id):
    join = Join.objects.get(id=join_id)

    # used to render view
    run_id = run_id
    res_id = str(join.chef.restaurant.id)
    # used to render view

    # Join has completed track
    join.delete()
    return HttpResponseRedirect('/chef/home/' + run_id + '/' + res_id)
