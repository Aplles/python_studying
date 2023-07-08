from django import template

from models_app.models import Page

register = template.Library()


@register.simple_tag
def get_page(id_page, *args, **kwargs):
    return Page.objects.get(id=id_page).name
