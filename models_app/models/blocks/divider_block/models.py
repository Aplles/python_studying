# -*- coding: utf-8 -*-
from models_app.models import Block


class DividerBlock(Block):

    def __str__(self):
        return "Блок с отступом"

    class Meta:
        db_table = "divider_blocks"
        verbose_name = "Блок с отступом"
        verbose_name_plural = "Блоки с отступом"
