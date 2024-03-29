from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Picts
from .utils import DataMixin, AutofillMixin, EmployeePassesTestMixin

# Create your views here.


class PictsList(DataMixin, ListView):
    paginate_by = 10
    template_name = 'picts/picts_list.html'
    page_header = 'List of all pictures'
    model = Picts

    def get_queryset(self):
        if 'title' in self.request.GET:
            title_value = self.request.GET.get('title')
            return super().get_queryset().filter(title__startswith=title_value)
        return super().get_queryset()


class PictDetails(DataMixin, DetailView):
    template_name = 'picts/pict_details.html'
    page_header = 'Details of picture'
    single_element = True
    model = Picts


class PictAdd(EmployeePassesTestMixin, AutofillMixin, DataMixin, CreateView):
    template_name = 'picts/pict_add.html'
    page_header = 'Add a new picture'
    model = Picts
    fields = ["title", "pict", "description"]


class PictEdit(EmployeePassesTestMixin, AutofillMixin, DataMixin, UpdateView):
    template_name = 'picts/pict_add.html'
    page_header = 'Edit the picture'
    single_element = True
    model = Picts
    fields = ["title", "pict", "description"]


class PictDelete(EmployeePassesTestMixin, DataMixin, DeleteView):
    template_name = 'picts/pict_delete.html'
    page_header = 'Delete the picture'
    single_element = True
    model = Picts
    success_url = reverse_lazy("main_page")
