from django.contrib import admin

from models_app.models import ImageBlock


@admin.register(ImageBlock)
class ImageBlockAdmin(admin.ModelAdmin):
    pass
