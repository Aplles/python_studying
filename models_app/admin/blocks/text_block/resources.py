from django.contrib import admin

from models_app.models import TextBlock


@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
    pass
