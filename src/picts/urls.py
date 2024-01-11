from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictsList.as_view(), name='main_page'),
    path('add/', views.PictAdd.as_view(), name='pict_add'),
    path('edit/<slug:slug>/', views.PictEdit.as_view(), name='pict_edit'),
    path(
        'delete/<slug:slug>/',
        views.PictDelete.as_view(),
        name='pict_delete'),
    path('details/<slug:slug>/', views.PictDetails.as_view(), name='pict'),
]
