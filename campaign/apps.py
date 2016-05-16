# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CampaignConfig(AppConfig):
    name = 'campaign'
    verbose_name = _("Campaign Management")
