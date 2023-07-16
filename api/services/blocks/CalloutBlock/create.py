from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page


class CalloutBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("CalloutBlock_new", None):
            for callout_block_index in self.data.get("CalloutBlock_new"):
                pass
