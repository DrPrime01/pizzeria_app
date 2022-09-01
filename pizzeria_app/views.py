from multiprocessing import context
from django.shortcuts import render
from .models import Pizza

# Create your views here.
def homepage(request, *args, **kwargs):
    """Homepage"""
    return render(request, "index.html", {})

def pizzas(request, *args, **kwargs):
    """Hello world page view"""
    pizza = Pizza.objects.order_by('date_added')
    context = {'pizza': pizza}
    return render(request, 'pizzas.html', context)

def pizza_toppings(request, pizza_id, *args, **kwargs):
    """Page for the pizza toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.toppings_set.all()
    context = {'pizza': pizza, 'topping': topping}
    return render(request, "pizza_toppings.html", context)