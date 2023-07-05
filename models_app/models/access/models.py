# -*- coding: utf-8 -*-
from django.db import models

from models_app.models.page.models import Page
from models_app.models.user.models import User


class Access(models.Model):
    page = models.ForeignKey(Page, blank=True, null=True,
                             on_delete=models.CASCADE,
                             verbose_name='Страница',
                             related_name='access_page')
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='access_user')

    def __str__(self):
        return f"{self.user.username}-{self.page.name}"

    class Meta:
        db_table = 'access'
        verbose_name = 'Доступ'
        verbose_name_plural = 'Доступы'
