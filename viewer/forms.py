from django.forms import ModelForm

from .models import MagicalItem

class ShopWindow(ModelForm):

    class Meta:
        model = MagicalItem
        include = ['name', 'rarity', 'attunemnet', 'slot',
                   'value', 'description', 'benefits',
                  ]
        
