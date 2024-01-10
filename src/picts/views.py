from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Picts

# Create your views here.

class PictsList(ListView):
    template_name = 'picts/picts_list.html'
    model = Picts
