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
        if self.data.get("CalloutBlock_new", None):
            for callout_block_index in range(int(self.data.get("CalloutBlock_new"))):
                position = next(self._positions())
                CalloutBlock.objects.create(
                    text=self.data.get(f"CalloutBlock_{position}_text"),
                    image=self.data.get(f"CalloutBlock_{position}_image"),
                    position=position,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [
            key for key in self.data.keys()
            if "CalloutBlock" in key and key != "CalloutBlock_new"
        ]:
            yield item.split("_")[1]
