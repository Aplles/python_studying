from django.contrib import admin

from models_app.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass