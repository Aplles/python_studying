# -*- coding: utf-8 -*-
from django.db import models

from models_app.models import Block


class CalloutBlock(Block):
    text = models.TextField(
        verbose_name="Текст"
    )
    image = models.ImageField(
        upload_to="callout_image_block/",
        verbose_name="Картинка"
    )

    def __str__(self):
        return "Блок с картинкой и текстом"

    class Meta:
        db_table = "callout_blocks"
        verbose_name = "Блок с картинкой и текстом"
        verbose_name_plural = "Блоки с картинкой и текстом"
