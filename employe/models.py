from django.db import models

class Employe(models.Model):
    name = models.CharField(db_index=True, max_length=100, verbose_name='Имя')
    age = models.IntegerField(db_index=True, verbose_name='Год рождения')
    salary = models.IntegerField(db_index=True, verbose_name='Зарплата')
    skill = models.TextField(db_index=True, blank=True, verbose_name='Навыки')
    image = models.ImageField(upload_to='image/%y/%m/%d')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    public = models.BooleanField(default=True, verbose_name='Опубликованно')