from django.shortcuts import render
from .models import Runner
from manager.models import Restaurant
from user.models import Order
from django.http import HttpResponseRedirect
from chef.models import Join


def render_orders(request, runner_id, res_id):
    res = Restaurant.objects.get(id=res_id)
    runner = Runner.objects.filter(restaurant=res).get(runner_id=runner_id)
    joins = Join.objects.filter(restaurant=res, ready=True).order_by('updated_at')
    orders = Order.objects.filter(restaurant=res).order_by('updated_at')
    return render(request, 'runner-orders.html', {'runner': runner, 'res': res_id, 'joins': joins, 'orders': orders})


def dish_complete(request, run_id, join_id, res_id):
    join = Join.objects.get(id=join_id)
    # Join has completed track
    join.delete()
    return HttpResponseRedirect('/runner/home/' + run_id + '/' + res_id)


def pay_bill(request, run_id, res_id, order_id):
    order = Order.objects.get(id=order_id)
    order.payment.has_payed = True
    order.payment.wants_to_pay = False
    order.payment.save()
    return HttpResponseRedirect('/runner/home/' + run_id + '/' + res_id)
