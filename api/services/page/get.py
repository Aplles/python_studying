from functools import lru_cache

import service_objects.fields
from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Page, User, Access


class GetPageService(ServiceWithResult):
    id = forms.UUIDField()
    user = service_objects.fields.ModelField(User)

    def process(self):
        self.result = {
            'page': self._get_page,
            'themes': self._get_themes
        }
        return self

    @property
    @lru_cache()
    def _get_page(self):
        return Page.objects.get(id=self.cleaned_data["id"])

    @property
    def _get_themes(self):
        themes = Page.objects.filter(parent_page=self._get_page)
        for theme in themes:
            theme.lock = not theme.name in self._get_access_pages
        return themes

    @property
    @lru_cache()
    def _get_access_pages(self):
        return Access.objects.select_related('page').filter(
            user=self.cleaned_data['user']
        ).values_list('page__name', flat=True)
