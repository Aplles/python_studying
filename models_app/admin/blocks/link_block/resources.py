from django.contrib import admin

from models_app.models import LinkBlock


@admin.register(LinkBlock)
class LinkBlockAdmin(admin.ModelAdmin):
    pass
