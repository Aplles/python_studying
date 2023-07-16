from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page


class TextBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        return self

    def _create(self):
        pass
