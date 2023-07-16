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
            for link_block_index in range(int(self.data.get("LinkBlock_new"))):
                position = self._positions()
                LinkBlock.objects.create(
                    page_link=Page.objects.get(id=self.data.get(f"LinkBlock_{position}_text")),
                    position=position,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [value for key, value in self.data.keys() if "LinkBlock" in key]:
            yield item.split("_")[1]
