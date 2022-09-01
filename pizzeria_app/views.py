from django.urls import reverse
from multiprocessing import context
from django.shortcuts import render
from .models import Pizza
from django.http import HttpResponseRedirect
from .forms import PizzaForm, ToppingsForm

# Create your views here.
def homepage(request, *args, **kwargs):
    """Homepage"""
    return render(request, "index.html", {})

def pizzas(request, *args, **kwargs):
    """Hello world page view"""
    pizza = Pizza.objects.order_by('date_added')
    context = {'pizza': pizza}
    return render(request, "pizzas.html", context)

def pizza_toppings(request, pizza_id, *args, **kwargs):
    """Page for the pizza toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    topping = pizza.toppings_set.all()
    context = {'pizza': pizza, 'topping': topping}
    return render(request, "pizza_toppings.html", context)

def new_pizza(request, *args, **kwargs):
    """Page to add new Pizza"""
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('pizzas'))
    context = {'form': form}
    return render(request, "new_pizza.html", context)

def new_toppings(request, pizza_id, *args, **kwargs):
    """Page to add toppings for each pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingsForm()
    else:
        form = ToppingsForm(data=request.POST)
        if form.is_valid:
            new_toppings = form.save(commit=False)
            new_toppings.pizza = pizza
            new_toppings.save()
            return HttpResponseRedirect(reverse('pizza_toppings', args=[pizza_id]))
    context = {'form': form, 'pizza': pizza}
    return render(request, "new_toppings.html", context)
