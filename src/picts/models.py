from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Picts(models.Model):
    title = models.CharField(max_length=255)
    #photo = models.ImageField(upload_to="/picts/%Y/%m/%d/", default=None, blank=True, null=True)

    description = models.TextField(blank=True) # Описание картинки
    size = models.CharField(max_length=255) # Размер картинки
    main_color = models.CharField(max_length=7) # Преобладающий цвет
    average_color = models.CharField(max_length=7) # Средний цвет изображения
    color_palette = models.CharField(max_length=255) # Цветовая палитра

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None)
