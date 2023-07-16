from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import TextBlock


class TextBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        return self

    def _create(self):
        if self.data.get("TextBlock_TEXT_new", None):
            for text_block_index in self.data.get("TextBlock_new"):
                position = self._positions()
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_TEXT_{position}_text'],
                    type=TextBlock.TEXT,
                    position=position,
                    page=self.cleaned_data['page']
                )
        elif self.data.get("TextBlock_CODE_new", None):
            for text_block_index in self.data.get("TextBlock_CODE_new"):
                position = self._positions()
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_CODE_{position}_text'],
                    type=TextBlock.CODE_TEXT,
                    position=position,
                    page=self.cleaned_data['page']
                )
        elif self.data.get("TextBlock_HEADERTEXT_new", None):
            for text_block_index in self.data.get("TextBlock_HEADERTEXT_new"):
                position = self._positions()
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_HEADERTEXT_{position}_text'],
                    type=TextBlock.HEADER_TEXT,
                    position=position,
                    page=self.cleaned_data['page']
                )
        elif self.data.get("TextBlock_QUOTETEXT_new", None):
            for text_block_index in self.data.get("TextBlock_QUOTETEXT_new"):
                position = self._positions()
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_QUOTETEXT_{position}_text'],
                    type=TextBlock.QUOTE_TEXT,
                    position=position,
                    page=self.cleaned_data['page']
                )

    def _positions(self):
        for item in [value for key, value in self.data.keys() if "TextBlock" in key]:
            yield item.split("_")[1]
