from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Page


class GetThemeService(ServiceWithResult):
    id = forms.UUIDField()

    def process(self):
        self.result = self._get_page
        return self

    @property
    def _get_page(self):
        return Page.objects.get(id=self.cleaned_data["id"])
