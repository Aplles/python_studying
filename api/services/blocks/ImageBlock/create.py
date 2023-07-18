from django.contrib.contenttypes.models import ContentType
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import ImageBlock


class ImageBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("ImageBlock_image_new", None):
            for image_block_index in range(int(self.data.get("ImageBlock_image_new"))):
                position = next(self._positions())
                ImageBlock.objects.create(
                    image=self.files.get(f"ImageBlock_{position}_image"),
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(ImageBlock).id,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [
            key for key in self.files.keys()
            if "ImageBlock" in key and key != "ImageBlock_image_new"
        ]:
            yield item.split("_")[1]
