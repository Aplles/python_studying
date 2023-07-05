from django.contrib import admin

from models_app.models import Block


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass
