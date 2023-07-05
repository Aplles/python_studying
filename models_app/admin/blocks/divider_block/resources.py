from django.contrib import admin

from models_app.models import DividerBlock


@admin.register(DividerBlock)
class DividerBlockAdmin(admin.ModelAdmin):
    pass
