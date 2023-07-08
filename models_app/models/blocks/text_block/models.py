# -*- coding: utf-8 -*-
from django.db import models

from models_app.models import Block


class TextBlock(Block):

    TEXT = "TEXT"
    CODE_TEXT = "CODE"
    HEADER_TEXT = "HEADERTEXT"
    QUOTE_TEXT = "QUOTETEXT"

    TYPE = [
        (TEXT, "Текст"),
        (CODE_TEXT, "Текст с кодом"),
        (HEADER_TEXT, "Заголовок"),
        (QUOTE_TEXT, "Поясняющий блок"),
    ]
    text = models.TextField(
        verbose_name="Текст"
    )
    type = models.CharField(
        choices=TYPE,
        default=TEXT,
        max_length=11,
        verbose_name="Тип блока"
    )

    def __str__(self):
        return "Блок с текстом"

    class Meta:
        db_table = "text_blocks"
        verbose_name = "Блок с текстом"
        verbose_name_plural = "Блоки с текстом"
