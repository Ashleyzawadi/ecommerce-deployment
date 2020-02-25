from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Category

# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'home.html'



