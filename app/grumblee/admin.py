# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.apps import apps
app = apps.get_app_config('grumblee')
for model_name, model in app.models.items():
    admin.site.register(model)
