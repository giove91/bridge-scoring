# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(ResearchView, self).get_context_data(**kwargs)
        # context['papers'] = Paper.objects.all()
        return context
