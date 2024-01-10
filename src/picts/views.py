from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Picts
from .utils import DataMixin

# Create your views here.

class PictsList(DataMixin, ListView):
    template_name = 'picts/picts_list.html'
    page_header = 'List of all pictures'
    model = Picts

class PictDetails(DataMixin, DetailView):
    template_name = 'picts/pict_details.html'
    page_header = 'Details of picture'
    model = Picts

class PictAdd(DataMixin, CreateView):
    template_name = 'picts/pict_add.html'
    page_header = 'Add a new picture'
    model = Picts
    fields = ["title", "pict", "description", "slug"]
