# Generated by Django 4.0 on 2023-07-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0003_alter_linkblock_page_link_alter_textblock_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='icon',
            field=models.ImageField(default=1, upload_to='image_page/', verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]