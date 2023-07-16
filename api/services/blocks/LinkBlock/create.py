from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import LinkBlock


class LinkBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("LinkBlock_new", None):
            for link_block_index in self.data.get("LinkBlock_new"):
                LinkBlock.objects.create(
                    page_link=Page.objects.get(id=self.data.get(f"LinkBlock_{link_block_index}_text"))
                )
