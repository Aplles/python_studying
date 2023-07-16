from functools import lru_cache

from django import forms
from django.db.models import Q
from service_objects.services import ServiceWithResult

from models_app.models import Page


class GetThemeService(ServiceWithResult):
    id = forms.UUIDField()

    def process(self):
        self.result = {
            'theme': self._get_theme_page,
            'blocks': self._get_blocks
        }
        return self

    @property
    @lru_cache()
    def _get_theme_page(self):
        return Page.objects.get(id=self.cleaned_data["id"])

    @property
    def _get_blocks(self):
        blocks = self._get_theme_page.blocks.all()
        if self.data.get('search'):
            return blocks.filter(
                Q(textblock__text__icontains=self.data['search']) |
                Q(calloutblock__text__icontains=self.data['search']) |
                Q(linkblock__page_link__name__icontains=self.data['search'])
            )
        return self._get_theme_page.blocks.all().order_by('position')
