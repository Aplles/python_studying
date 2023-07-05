# -*- coding: utf-8 -*-
import uuid

from django.db import models
from polymorphic.models import PolymorphicModel


class Block(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="Позиция",
        null=True,
        blank=True,
    )
    page = models.ForeignKey(
        "Page",
        related_name="blocks",
        related_query_name="block",
        verbose_name="Страница",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = "blocks"
        ordering = [
            "position",
        ]
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"
