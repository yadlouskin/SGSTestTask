from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictsList.as_view()),
    path('details/<slug:slug>/', views.PictDetails.as_view(), name='pict'),
]
