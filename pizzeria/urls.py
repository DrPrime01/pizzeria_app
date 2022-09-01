"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizzeria_app.views import homepage, pizzas, pizza_toppings, new_pizza, new_toppings #use this to avoid making mistakes with many imported views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('pizzas/', pizzas, name="pizzas"),
    path('pizza_toppings/<int:pizza_id>/', pizza_toppings, name="pizza_toppings"),
    path('new_pizza/', new_pizza, name="new_pizza"),
    path('new_toppings/<int:pizza_id>/', new_toppings, name="new_toppings")
]
