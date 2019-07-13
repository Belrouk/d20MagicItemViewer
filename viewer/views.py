from __future__ import unicode_literals
from django.shortcuts import render
from .models import MagicalItem

from .forms import ItemViewerForm, ItemCreatorView, ItemEditorView


def home_view(
        request, form_class=ItemViewerForm, template="viewer/home.html",
        extra_context=None, when=None, *args, **kwargs):
        form=form_class(
            data=request.POST or None,
            files=request.FILES or None
            )
        items = MagicalItem.objects.all()

        if request.POST:
            print("Valid:", form.is_valid())
            print("Bound:", form.is_bound)
            print(form.non_field_errors())
            if form.is_valid():
                import pudb; pudb.set_trace()


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

        if request.POST:
            #import pudb; pudb.set_trace()
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
