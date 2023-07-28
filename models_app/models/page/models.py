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
    icon = models.ImageField(
        upload_to="image_page/",
        verbose_name="Иконка",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'pages'
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
