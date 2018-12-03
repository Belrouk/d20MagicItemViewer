# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Model, CharField, TextField

from djrichtextfield.models import RichTextField


class MagicalItem(Model):

    name = CharField(max_length=200)
    rarity = CharField(max_length=100)
    attunement = CharField(max_length=100)
    slot = CharField(max_length=100)
    value = CharField(max_length=100)
    description = TextField()
    benefits = RichTextField()

    def __str__(self):
        return self.name
