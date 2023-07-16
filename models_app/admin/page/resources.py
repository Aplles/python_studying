from django.contrib import admin

from models_app.models import Page, ImageBlock, DividerBlock
from models_app.models import TextBlock
from models_app.models import CalloutBlock
from models_app.models import LinkBlock


class TextBlockInline(admin.TabularInline):
    model = TextBlock
    extra = 0


class CalloutBlockInline(admin.TabularInline):
    model = CalloutBlock
    extra = 0


class LinkBlockInline(admin.TabularInline):
    model = LinkBlock
    extra = 0
    fk_name = "page"


class ImageBlockInline(admin.TabularInline):
    model = ImageBlock
    extra = 0


class DividerBlockInline(admin.TabularInline):
    model = DividerBlock
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [
        TextBlockInline,
        CalloutBlockInline,
        LinkBlockInline,
        DividerBlockInline,
        ImageBlockInline
    ]
