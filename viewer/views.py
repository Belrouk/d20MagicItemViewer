# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import MagicalItem


# Create your views here.
def home_view(
        request, form_class=None, template="viewer/home.html",
        extra_context=None, when=None, *args, **kwargs):
        items = MagicalItem.objects.all()[0]
        context = {
            'items': items
        }
        return render(request, template, context=context)
