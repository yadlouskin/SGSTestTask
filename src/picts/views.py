from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Picts
from .utils import DataMixin

# Create your views here.

class PictsList(DataMixin, ListView):
    paginate_by = 10
    template_name = 'picts/picts_list.html'
    page_header = 'List of all pictures'
    model = Picts

class PictDetails(DataMixin, DetailView):
    template_name = 'picts/pict_details.html'
    page_header = 'Details of picture'
    single_element = True
    model = Picts

class PictAdd(DataMixin, CreateView):
    template_name = 'picts/pict_add.html'
    page_header = 'Add a new picture'
    model = Picts
    fields = ["title", "pict", "description"]

class PictEdit(DataMixin, UpdateView):
    template_name = 'picts/pict_add.html'
    page_header = 'Edit the picture'
    single_element = True
    model = Picts
    fields = ["title", "pict", "description"]

class PictDelete(DataMixin, DeleteView):
    template_name = 'picts/pict_delete.html'
    page_header = 'Delete the picture'
    single_element = True
    model = Picts
    success_url = reverse_lazy("main_page")
