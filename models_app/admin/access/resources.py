from django.contrib import admin

from models_app.models import Access


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    pass