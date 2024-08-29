from django.contrib import admin

from models_app.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_page', 'main_page')
    fields = (
        'id',
        'name',
        'parent_page',
        'main_page',
        'icon',
        'created_at',
        'updated_at',
    )
    ordering = ('parent_page', 'name')
    list_filter = ('parent_page', )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    actions = ['remove_blocks']

    @admin.action(description="Удалить все блоки на странице")
    def remove_blocks(self, request, queryset):
        for page in queryset:
            for block in page.blocks.all():
                block.delete()

