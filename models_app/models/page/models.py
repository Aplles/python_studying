# -*- coding: utf-8 -*-
import uuid

from django.db import models


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, verbose_name='Страница')
    parent_page = models.ForeignKey('self', blank=True, null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Родительская страница',
                                    related_name='pages')

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        db_table = 'pages'
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
