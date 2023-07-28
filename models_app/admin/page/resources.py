from django.contrib import admin

from models_app.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    list_display = ('id', 'name', 'parent_page')

    ordering = ('parent_page', 'name')

    fields = (
        'id',
        'name',
        'parent_page',
        'icon',
        'created_at',
        'updated_at',
    )

    list_filter = ('parent_page', )
