from django.forms import ModelForm

from .models import MagicalItem
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Fieldset, Layout

class ShopWindow(ModelForm):

    class Meta:
        model = MagicalItem
        include = ['name', 'rarity', 'attunemnet', 'slot',
                   'value', 'description', 'benefits',
                  ]
