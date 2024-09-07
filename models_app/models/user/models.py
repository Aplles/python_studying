# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = "models_app"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
