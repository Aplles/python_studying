# -*- coding: utf-8 -*-
from django.db import models

from models_app.models import Block


class LinkBlock(Block):
    page_link = models.ForeignKey(
        "Page",
        on_delete=models.CASCADE,
        related_name="links",
        verbose_name="Страница (ссылка)"
    )

    def __str__(self):
        return "Блок с ссылкой"

    class Meta:
        db_table = "line_blocks"
        verbose_name = "Блок с ссылкой"
        verbose_name_plural = "Блоки с ссылкой"
