from functools import lru_cache

from service_objects.services import ServiceWithResult
from service_objects.services import ServiceOutcome

from api.services.blocks.CalloutBlock.create import CalloutBlockCreateService
from api.services.blocks.DividerBlock.create import DividerBlockCreateService
from api.services.blocks.ImageBlock.create import ImageBlockCreateService
from api.services.blocks.LinkBlock.create import LinkBlockCreateService
from api.services.blocks.TextBlock.create import TextBlockCreateService

from models_app.models import Page


class FillPageService(ServiceWithResult):
    LIST_BLOCKS = {
        "TextBlock": TextBlockCreateService,
        "CalloutBlock": CalloutBlockCreateService,
        "LinkBlock": LinkBlockCreateService,
        "ImageBlock": ImageBlockCreateService,
        "DividerBlock": DividerBlockCreateService,
    }

    def process(self):
        self.fill()
        return self

    @property
    @lru_cache
    def _page(self):
        return Page.objects.get(id=self.data["page_id"])

    def _fill(self):
        for block in self.data.keys():
            type_block = block.split("_")[0]
            if type_block in self.LIST_BLOCKS:
                ServiceOutcome(
                    self.LIST_BLOCKS[type_block],
                    self.data | {
                        "page": self._page
                    },
                )
