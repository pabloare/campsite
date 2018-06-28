from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Chef
from manager.models import Restaurant


def render_orders():
    return render('chef-orders.html')
