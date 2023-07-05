from django.contrib import admin

from models_app.models import CalloutBlock


@admin.register(CalloutBlock)
class CalloutBlockAdmin(admin.ModelAdmin):
    pass
