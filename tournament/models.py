# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import Counter
from django.db import models

from score_to_imps import score_to_imps


class Couple(models.Model):
    name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.name


class Board(models.Model):
    number = models.IntegerField()
    
    def __str__(self):
        return "Board %d" % self.number
    
    class Meta:
        ordering = ('number',)
    
    
    def get_imps(self):
        imps = Counter()
        
        for result in self.results:
            couples = result.couples()
            score = result.score
            
            for r in self.results:
                s = r.score
                score_to_imps(score-s)


class Result(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    ns_couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="ns_results")
    ew_couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name="ew_results")
    score = models.IntegerField(help_text="Positive for NS, negative for EW")
    
    class Meta:
        ordering = ('board',)
        unique_together = [('board', 'ns_couple'), ('board', 'ew_couple')]
    
    
    def couples(self):
        return (self.ns_couple, self.ew_couple)
