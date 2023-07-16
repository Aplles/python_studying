from functools import lru_cache

from django import forms
from django.db.models import Value
from service_objects.services import ServiceWithResult

from models_app.models import Page, User, Access


class GetPageService(ServiceWithResult):
    id = forms.UUIDField()
    user_pk = forms.IntegerField(required=False)

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
        if not self.cleaned_data['user_pk']:
            return themes.annotate(lock=Value("Lock"))
        for theme in themes:
            theme.lock = not theme.name in self._get_access_pages
        return themes

    @property
    @lru_cache()
    def _get_access_pages(self):
        return Access.objects.select_related('page').filter(
            user=self._get_user
        ).values_list('page__name', flat=True)

    @property
    @lru_cache()
    def _get_user(self):
        return User.objects.get(pk=self.cleaned_data['user_pk'])
