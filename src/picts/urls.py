from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictsList.as_view()),
    path('add/', views.PictAdd.as_view(), name='pict_add'),
    path('details/<slug:slug>/', views.PictDetails.as_view(), name='pict'),
]
