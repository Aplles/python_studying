from django.contrib.contenttypes.models import ContentType
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import DividerBlock


class DividerBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("DividerBlock_new", None):
            for link_block_index in range(int(self.data.get("DividerBlock_new"))):
                DividerBlock.objects.create(
                    position=next(self._positions()),
                    polymorphic_ctype_id=ContentType.objects.get_for_model(DividerBlock).id,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [
            key for key in self.data.keys()
            if "DividerBlock" in key and key != "DividerBlock_new"
        ]:
            yield item.split("_")[1]
