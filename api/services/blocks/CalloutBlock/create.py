from django.contrib.contenttypes.models import ContentType
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import CalloutBlock


class CalloutBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("CalloutBlock_text_new", None):
            for callout_block_index in range(int(self.data.get("CalloutBlock_text_new"))):
                position = next(self._positions())
                CalloutBlock.objects.create(
                    text=self.data.get(f"CalloutBlock_{position}_text"),
                    image=self.files.get(f"CalloutBlock_{position}_image"),
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(CalloutBlock).id,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [
            key for key in self.data.keys()
            if "CalloutBlock" in key and key not in ["CalloutBlock_text_new", "CalloutBlock_image_new"]
        ]:
            yield item.split("_")[1]
