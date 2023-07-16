from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page


class DividerBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        return self

    def _create(self):
        if self.data.get("DividerBlock_new", None):
            for divider_block_index in self.data.get("DividerBlock_new"):
                pass
