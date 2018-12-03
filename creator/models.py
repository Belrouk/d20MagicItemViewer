# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Model, CharField


class Creator(Model):

    """
    put user stuff here. user django user model. we need nothing special
    """
    user = CharField(max_length=20, null=True, blank=True, default="")
