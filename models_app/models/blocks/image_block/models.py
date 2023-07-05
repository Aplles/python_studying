# -*- coding: utf-8 -*-
from django.db import models

from models_app.models import Block


class ImageBlock(Block):
    image = models.ImageField(
        upload_to="image_block/",
        verbose_name="Картинка"
    )

    def __str__(self):
        return "Блок с картинкой"

    class Meta:
        db_table = "image_blocks"
        verbose_name = "Блок с картинкой"
        verbose_name_plural = "Блоки с картинкой"
