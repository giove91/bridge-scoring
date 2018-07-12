# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ('name', 'imps')

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('board', 'ns_couple', 'ew_couple')
    # list_display = ('board', 'ns_couple', 'ew_couple', 'score', 'ns_imps')
    list_filter = ('board',)
