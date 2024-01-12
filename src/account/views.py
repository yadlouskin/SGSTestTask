from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse

# Create your views here.


User.get_absolute_url = lambda self: reverse(
    'user_details', kwargs={'pk': self.id})


class UserList(ListView):
    template_name = 'account/user_list.html'
    model = User
    extra_context = {"page_header": "List of users"}


class UserDetails(DetailView):
    template_name = 'account/user_details.html'
    model = User
    extra_context = {"page_header": "User details"}


class UserAdd(CreateView):
    template_name = 'account/user_add.html'
    model = User
    extra_context = {"page_header": "Add user"}
    fields = [
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'groups']
