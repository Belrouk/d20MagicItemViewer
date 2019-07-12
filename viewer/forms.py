from django.forms import (
    BooleanField,
    CharField,
    ChoiceField,
    Form,
    IntegerField,
    NumberInput,
    Textarea,
    ModelForm


    )
from djrichtextfield.widgets import RichTextWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout, Div,  Submit, Row, Column
from django.utils.translation import ugettext_lazy as _
from .models import MagicalItem
from django.core.exceptions import ValidationError

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

class ItemCreatorView(ModelForm):
    rarity_filter = ChoiceField(choices=MagicalItem.RARITY_LEVEL, required=True)
    attunement_filter = ChoiceField(choices=MagicalItem.ATTUNEMENT, required=True)
    item_filter = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=True)
    name = CharField(max_length=200, required=True, widget=Textarea(attrs={'rows': 1, 'cols':80}))
    campaign = CharField(max_length=200, required=False, widget=Textarea(attrs={'rows': 1, 'cols':80}))
    value = IntegerField(min_value=0, required=False)
    description = CharField(max_length=5000, required=True,
                            widget=Textarea(attrs={'rows': 5, 'cols':80}))
    benefits = CharField(widget=Textarea(attrs={'rows': 5, 'cols':80}), required=True)

    class Meta:
        model = MagicalItem
        fields = ['campaign','name','rarity','attunement','type','value',
                'description','benefits',
                ]

    def __init__(self, *args, **kwargs):
        super(ItemCreatorView, self).__init__(*args, **kwargs)
        self.fields["rarity_filter"].label = _("Rarity")
        self.fields["attunement_filter"].label = _("Requires Attunement")
        self.initial['attunement_filter'] = MagicalItem.YES
        self.fields["item_filter"].label = _("Item Type")
        self.fields["name"].label = _("Item Name")
        self.fields["campaign"].label = _("Campaign Title")

    def clean_rarity_filter(self):
        data = self.cleaned_data['rarity_filter']
        if int(data) == 0:
            raise ValidationError("Please choose a valid rarity choice")
        return data

    def clean_item_filter(self):
        data = self.cleaned_data['item_filter']
        if int(data) == 0:
            raise ValidationError("Please choose a valid item choice")
        return data

    def clean_attunement_filter(self):
        data = self.cleaned_data['attunement_filter']
        if data is None:
            raise ValidationError("Please choose a valid attunement choice")
        return data

    def save(self, commit=True):        
        self.rarity = self.cleaned_data['rarity_filter']
        self.attunement = self.cleaned_data['attunement_filter']
        self.type = self.cleaned_data['item_filter']
        return super().save()
