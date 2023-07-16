from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import TextBlock


class TextBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        return self

    def _create(self):
        if self.data.get("TextBlock_new", None):
            for text_block_index in self.data.get("TextBlock_new"):
                pass

