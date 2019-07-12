from __future__ import unicode_literals
from django.shortcuts import render
from .models import MagicalItem

from .forms import ItemViewerForm, ItemCreatorView


def home_view(
        request, form_class=ItemViewerForm, template="viewer/home.html",
        extra_context=None, when=None, *args, **kwargs):


        items = MagicalItem.objects.all()
        context = {
            'item_list': items,
            'form': form_class
        }

        return render(request, template, context, *args, **kwargs)

def create_item_view(request, form_class=ItemCreatorView, template="viewer/create_item.html",
                    extra_context=None, when=None, *args, **kwargs):
        context = {
            "form": form_class
        }
        return render(request, template, context, *args, **kwargs)
