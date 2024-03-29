from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView

from .views import UserList, UserDetails, UserAdd, UserEdit, UserDelete


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='account/login.html',
        form_class=AuthenticationForm,
        extra_context={"page_header": "Login"}
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', login_required(TemplateView.as_view(
        template_name='account/main_user.html',
        extra_context={"page_header": "User main page"}
    )), name='main_user'),

    path('password-change/', PasswordChangeView.as_view(
        template_name='account/password_change_form.html',
        extra_context={"page_header": "Change your password"}
    ), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html',
        extra_context={"page_header": "Password changed"}
    ), name='password_change_done'),

    path('user_detail/<int:pk>/', UserDetails.as_view(), name='user_details'),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('add_user/', UserAdd.as_view(), name='add_user'),
    path('edit_user/<int:pk>/', UserEdit.as_view(), name='edit_user'),
    path('delete_user/<int:pk>/', UserDelete.as_view(), name='delete_user'),
]
