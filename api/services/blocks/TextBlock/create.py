from django.contrib.contenttypes.models import ContentType
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Page
from models_app.models import TextBlock


class TextBlockCreateService(ServiceWithResult):
    page = ModelField(Page)

    def process(self):
        self._create()
        return self

    def _create(self):
        if self.data.get("TextBlock_TEXT_new", None):
            for text_block_index in range(int(self.data.get("TextBlock_TEXT_new"))):
                position = next(self._positions_text_block())
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_TEXT_{position}_text'],
                    type=TextBlock.TEXT,
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(TextBlock).id,
                    page=self.cleaned_data['page']
                )
        if self.data.get("TextBlock_CODE_new", None):
            for text_block_index in range(int(self.data.get("TextBlock_CODE_new"))):
                position = next(self._positions_code_block())
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_CODE_{position}_text'],
                    type=TextBlock.CODE_TEXT,
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(TextBlock).id,
                    page=self.cleaned_data['page']
                )
        if self.data.get("TextBlock_HEADERTEXT_new", None):
            for text_block_index in range(int(self.data.get("TextBlock_HEADERTEXT_new"))):
                position = next(self._positions_header_text_block())
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_HEADERTEXT_{position}_text'],
                    type=TextBlock.HEADER_TEXT,
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(TextBlock).id,
                    page=self.cleaned_data['page']
                )
        if self.data.get("TextBlock_QUOTETEXT_new", None):
            for text_block_index in range(int(self.data.get("TextBlock_QUOTETEXT_new"))):
                position = next(self._positions_quote_text_block())
                TextBlock.objects.create(
                    text=self.data[f'TextBlock_QUOTETEXT_{position}_text'],
                    type=TextBlock.QUOTE_TEXT,
                    position=position,
                    polymorphic_ctype_id=ContentType.objects.get_for_model(TextBlock).id,
                    page=self.cleaned_data['page']
                )

    def _positions_text_block(self):
        for item in [
            key for key in self.data.keys()
            if "TextBlock_TEXT" in key and key != "TextBlock_TEXT_new"
        ]:
            yield item.split("_")[2]

    def _positions_code_block(self):
        for item in [
            key for key in self.data.keys()
            if "TextBlock_CODE" in key and key != "TextBlock_CODE_new"
        ]:
            yield item.split("_")[2]

    def _positions_header_text_block(self):
        for item in [
            key for key in self.data.keys()
            if "TextBlock_HEADERTEXT" in key and key != "TextBlock_HEADERTEXT_new"
        ]:
            yield item.split("_")[2]

    def _positions_quote_text_block(self):
        for item in [
            key for key in self.data.keys()
            if "TextBlock_QUOTETEXT" in key and key != "TextBlock_QUOTETEXT_new"
        ]:
            yield item.split("_")[2]
