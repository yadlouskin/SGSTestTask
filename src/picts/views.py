from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Picts

# Create your views here.

class PictsList(ListView):
    template_name = 'picts/picts_list.html'
    model = Picts

class PictDetails(DetailView):
    template_name = 'picts/pict_details.html'
    model = Picts

class PictAdd(CreateView):
    template_name = 'picts/pict_add.html'
    model = Picts
    fields = ["title", "pict", "description", "slug"]
