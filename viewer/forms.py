from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    Form,
    IntegerField,
    NumberInput,

    )
from djrichtextfield.widgets import RichTextWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout, Div,  Submit, Row, Column

from .models import MagicalItem

class ItemViewerForm(Form):
    rarity_filter = ChoiceField(choices=MagicalItem.RARITY_LEVEL, required=False)
    attunement_filter = ChoiceField(choices=MagicalItem.ATTUNEMENT, required=False)
    item_filter = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=False)

    class Meta:
        model = MagicalItem


    # def __init__(self, *args, **kwargs):
    #     super(ItemViewerForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('rarity_filter', css_class="form-group col-md-2 mb-0"),
    #             Column('attunement_filter', css_class="form-group col-md-2 mb-0"),
    #             Column('item_filter', css_class="form-group col-md-2 mb-0"),
    #             css_class="form-row container-fluid"
    #             ),
    #         Row(
    #             Column(Submit('submit', 'Search'), css_class="form-group col-md-2 mb-0"),
    #             css_class="form-row container-fluid align-bottom"
    #         )
    #
    #         )

class ItemCreatorView(Form):
    rarity_filter = ChoiceField(choices=MagicalItem.RARITY_LEVEL, required=True)
    attunement_filter = ChoiceField(choices=MagicalItem.ATTUNEMENT, required=True)
    item_filter = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=True)
    name = CharField(max_length=200, required=True)
    campaign = CharField(max_length=200, required=False)
    value = IntegerField(min_value=0, required=False)
    description = CharField(max_length=5000, required=True)
    benefits = CharField(widget=RichTextWidget())

    class Meta:
        model = MagicalItem
        fields = ["campaign", "name", "rarity", "attunement",
                  "type", "value", "description", "benefits"]
