# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db.models import Model, CharField, TextField, IntegerField, AutoField
from mezzanine.core.models import TimeStamped
from djrichtextfield.models import RichTextField


class MagicalItem(TimeStamped):
    """
    from TimeStamped:
        updated = models.DateTimeField(...)
        created = models.DateTimeField(...)
    """
    NOVALUE = 0
    ARMOR = 100
    POTION = 200
    RING = 300
    AMULET = 400
    ROD = 500
    SCROLL = 600
    STAFF = 700
    WAND = 800
    WEAPON = 900
    WONDEROUS_ITEM = 1000
    ITEM_TYPE = (
        (NOVALUE, _("-----")),
        (ARMOR, _('Armor')),
        (POTION, _('Potion')),
        (RING, _('Ring')),
        (AMULET, _('Amulet')),
        (ROD, _('Rod')),
        (SCROLL, _('Scroll')),
        (STAFF, _('Staff')),
        (WAND, _('Wand')),
        (WEAPON, _('Weapon')),
        (WONDEROUS_ITEM, _('Wonderous Item')),
        )

    COMMON = 10
    UNCOMMON = 20
    RARE = 30
    VERY_RARE = 40
    LEGENDARY = 50
    ARTIFACT = 600
    RARITY_LEVEL = (
        (NOVALUE, _("-----")),
        (COMMON, _('Common')),
        (UNCOMMON, _('Uncommon')),
        (RARE, _('Rare')),
        (VERY_RARE, _('Very Rare')),
        (LEGENDARY, _('Legendary')),
        (ARTIFACT, _('Artifact')),
    )
    NOVALUE_STR = None
    YES = "Yes"
    NO = "No"
    SPECIAL = "Special"
    ATTUNEMENT = (
        (NOVALUE_STR, _("-----")),
        (YES, _("Yes")),
        (NO, _('No')),
        (SPECIAL, _('Special'))
    )
    id = AutoField(primary_key=True)
    # Creator
    campaign = CharField(max_length=200, null=True, blank=True, default="")
    name = CharField(max_length=200, unique=True)
    rarity = IntegerField(verbose_name=_("Item Rarity"), choices=RARITY_LEVEL,
                          default=COMMON, null=True, blank=True)
    attunement = CharField(verbose_name=_("Requires Attunemnet"), choices=ATTUNEMENT,
                           max_length=10, default=YES, null=True, blank=True)
    type = IntegerField(verbose_name=_("Item type"), choices=ITEM_TYPE,
                        default=None, null=True, blank=True)
    value = CharField(max_length=100, null=True, blank=True, default=None)
    description = TextField()
    benefits = RichTextField()
    # tags

    def __str__(self):
        return self.name
