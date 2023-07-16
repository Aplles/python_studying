# Generated by Django 4.0 on 2023-07-16 15:31

from django.db import migrations
from django.db.migrations import RunPython

from conf.settings.django import env


def main_page(apps, schema_editor):
    Page = apps.get_model("models_app", "Page")
    main, create = Page.objects.get_or_create(
        id=env("MAIN_PAGE_UUID", cast=str),
        name="Главная страница",
    )
    Page.objects.get_or_create(
        id=env("PYTHON_BASIC_UUID", cast=str),
        name="Python основы",
        parent_page=main
    )
    Page.objects.get_or_create(
        id=env("PYTHON_OOP_UUID", cast=str),
        name="Python ООП",
        parent_page=main
    )
    Page.objects.get_or_create(
        id=env("DJANGO_UUID", cast=str),
        name="Django",
        parent_page=main
    )


class Migration(migrations.Migration):
    dependencies = [
        ('models_app', '0005_alter_page_icon'),
    ]

    operations = [
        RunPython(main_page),
    ]
