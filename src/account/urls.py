from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='account/login.html',
        form_class=AuthenticationForm,
        extra_context={"page_header": "Login"}
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', TemplateView.as_view(
        template_name = 'account/main_user.html',
        extra_context={"page_header": "User main page"}
    ), name='main_user')
]