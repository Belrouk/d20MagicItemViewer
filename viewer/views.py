from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import MagicalItem

from .forms import ItemViewerForm, ItemCreatorView, ItemEditorView
from .queries import ItemCollectionQuerySet as ICQS


def home_view(
        request, form_class=ItemViewerForm, template="viewer/home.html",
        extra_context=None, when=None, *args, **kwargs):
        form=form_class(
            data=request.POST or None,
            files=request.FILES or None
            )

        if "filter_items" in request.POST:
            print("Valid:", form.is_valid())
            print("Bound:", form.is_bound)
            print(form.non_field_errors())
            if form.is_valid():
                rarity = form.cleaned_data["rarity_filter"]
                type = form.cleaned_data["type_filter"]
                attunement = form.cleaned_data['attunement_filter']
                itemQuery = ICQS()
                items = itemQuery.filter_item_query(rarity=rarity, attunement=attunement, type=type)

        else:
            items = MagicalItem.objects.all()

        context = {
            'item_list': items,
            'form': form_class
        }

        return render(request, template, context, *args, **kwargs)

def create_item_view(request, form_class=ItemCreatorView, template="viewer/create_item.html",
                    extra_context=None, when=None, *args, **kwargs):
        form=form_class(
            data=request.POST or None,
            files=request.FILES or None
            )
        context = extra_context or {}

        if request.POST:
            print("Valid:", form.is_valid())
            print("Bound:", form.is_bound)
            print(form.non_field_errors())
            if form.is_valid():
                form.save()
                context.update({
                    "form": form,
                    "item_saved": True
                    })
                return render(request, template, context, *args, **kwargs)

        context.update({
            "form": form,
            "item_saved": False
            })

        return render(request, template, context, *args, **kwargs)

def edit_item_view(request, id, form_class=ItemEditorView, template="viewer/edit_item.html",
                    extra_context=None, when=None, *args, **kwargs):

        item = MagicalItem.objects.get(id=id)
        form=form_class(item=item,
            data=request.POST or None,
            files=request.FILES or None
            )
        context = extra_context or {}

        if "save_item" in request.POST:
            #import pudb; pudb.set_trace()
            if form.is_valid():
                form.save()
                context.update({
                    "form": form,
                    "item_saved": True
                    })
                return render(request, template, context, *args, **kwargs)

        if "delete_item" in request.POST:
            item.delete()
            return redirect('items:item_viewer')
        if "back" in request.POST:
            item.delete()
            return redirect('items:item_viewer')

        context.update({
            "form": form,
            "item_saved": False
            })

        return render(request, template, context, *args, **kwargs)
