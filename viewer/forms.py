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
    type_filter = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=False)

    def clean_rarity_filter(self):
        data = self.cleaned_data['rarity_filter']
        if data is None or data is '':
            data = 0
        return data

    def clean_attunement_filter(self):
        data = self.cleaned_data['attunement_filter']
        if data is None or data is '':
            data = None
        return data

    def clean_type_filter(self):
        data = self.cleaned_data['type_filter']
        if data is None or data is '':
            data = 0
        return data


class ItemCreatorView(ModelForm):
    rarity = ChoiceField(choices=MagicalItem.RARITY_LEVEL, required=True)
    attunement = ChoiceField(choices=MagicalItem.ATTUNEMENT, required=True)
    type = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=True)
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
        self.fields["rarity"].label = _("Rarity")
        self.fields["attunement"].label = _("Requires Attunement")
        self.initial['attunement'] = MagicalItem.YES
        self.fields["type"].label = _("Item Type")
        self.fields["name"].label = _("Item Name")
        self.fields["campaign"].label = _("Campaign Title")

    def clean_rarity(self):
        data = self.cleaned_data['rarity']
        if int(data) == 0:
            raise ValidationError("Please choose a valid rarity choice")
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        if int(data) == 0:
            raise ValidationError("Please choose a valid type choice")
        return data

    def clean_attunement(self):
        data = self.cleaned_data['attunement']
        if data is None:
            raise ValidationError("Please choose a valid attunement choice")
        return data

    def save(self, commit=True):
        return super().save(commit)

class ItemEditorView(ModelForm):
    rarity = ChoiceField(choices=MagicalItem.RARITY_LEVEL, required=True)
    attunement = ChoiceField(choices=MagicalItem.ATTUNEMENT, required=True)
    type = ChoiceField(choices=MagicalItem.ITEM_TYPE, required=True)
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

    def __init__(self, item, *args, **kwargs):
        super(ItemEditorView, self).__init__(*args, **kwargs)
        self.instance = item
        self.fields["rarity"].label = _("Rarity")
        self.fields["attunement"].label = _("Requires Attunement")
        self.fields["type"].label = _("Item Type")
        self.fields["name"].label = _("Item Name")
        self.fields["campaign"].label = _("Campaign Title")

        self.initial['campaign'] = item.campaign
        self.initial['name'] = item.name
        self.initial['rarity'] = item.rarity
        self.initial['attunement'] = item.attunement
        self.initial['type'] = item.type
        self.initial['value'] = item.value
        self.initial['description'] = item.description
        self.initial['benefits'] = item.benefits


    def clean_rarity(self):
        data = self.cleaned_data['rarity']
        if int(data) == 0:
            raise ValidationError("Please choose a valid rarity choice")
        return data

    def clean_type(self):
        data = self.cleaned_data['type']
        if int(data) == 0:
            raise ValidationError("Please choose a valid type choice")
        return data

    def clean_attunement(self):
        data = self.cleaned_data['attunement']
        if data is None:
            raise ValidationError("Please choose a valid attunement choice")
        return data

    def save(self, commit=True):
        #import pudb; pudb.set_trace()
        return super().save(commit)
