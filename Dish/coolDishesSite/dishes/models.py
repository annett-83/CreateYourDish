from django.db import models


class Dishes(models.Model):
    title = models.CharField(max_length=255)  # загаловок
    content = models.TextField(blank=True)  # содержание рецепта
    time_create = models.DateTimeField(auto_now_add=True)  # время создания записи
    time_update = models.DateTimeField(auto_now=True)  # время изменения записи
    is_published = models.BooleanField(default=True)  # опубликована или не опубликована
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # ссылка на категорию

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # первое, второе или третье блюдо

    def __str__(self):
        return self.name

# Create your models here.
