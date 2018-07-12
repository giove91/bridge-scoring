# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        scoreboard = sorted(((couple, couple.imps()) for couple in Couple.objects.all()), key=lambda x: -x[1])
        
        # compute ranking
        ranks = {}
        prev = None
        for i, (k,v) in enumerate(scoreboard):
            if v != prev:
                place, prev = i+1, v
            ranks[k] = place
        
        
        boards = Board.objects.all()
        
        # compute imps on boards
        boards_imps = {couple: [board.couple_imps(couple) for board in boards] for couple in Couple.objects.all()}
        
        context['boards'] = boards
        context['scoreboard'] = [(couple, imps, ranks[couple], boards_imps[couple]) for (couple, imps) in scoreboard]
        
        return context
