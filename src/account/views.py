from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.


class UserList(ListView):
    template_name = 'account/user_list.html'
    model = User
    extra_context = {"page_header": "List of users"}


class UserDetails(DetailView):
    template_name = 'account/user_details.html'
    model = User
    extra_context = {"page_header": "User details"}
