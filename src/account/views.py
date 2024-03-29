from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy

from .utils import AdminRolePassesTestMixin

# Create your views here.


User.get_absolute_url = lambda self: reverse(
    'user_details', kwargs={'pk': self.id})


class UserList(AdminRolePassesTestMixin, ListView):
    template_name = 'account/user_list.html'
    model = User
    extra_context = {"page_header": "List of users"}


class UserDetails(AdminRolePassesTestMixin, DetailView):
    template_name = 'account/user_details.html'
    model = User
    extra_context = {"page_header": "User details"}


class UserAdd(AdminRolePassesTestMixin, CreateView):
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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password'))
        return super().form_valid(form)


class UserEdit(AdminRolePassesTestMixin, UpdateView):
    template_name = 'account/user_add.html'
    model = User
    extra_context = {"page_header": "Edit user"}
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'groups']


class UserDelete(AdminRolePassesTestMixin, DeleteView):
    template_name = 'account/user_delete.html'
    model = User
    extra_context = {"page_header": "Delete user"}
    success_url = reverse_lazy("user_list")
