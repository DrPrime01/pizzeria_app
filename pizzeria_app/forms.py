from dataclasses import field
from pyexpat import model
from django import forms
from .models import Pizza, Toppings

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'text': ''}


class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = ['name']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput}