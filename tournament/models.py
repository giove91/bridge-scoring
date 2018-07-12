# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import Counter
from django.db import models

from score_to_imps import score_to_imps


class Couple(models.Model):
    name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.name

    
    def imps(self):
        return sum(result.couple_imps(self) for result in Result.objects.all())


class Board(models.Model):
    number = models.IntegerField()
    
    def __str__(self):
        return "Board %d" % self.number
    
    class Meta:
        ordering = ('number',)
    


class Result(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    ns_couple = models.ForeignKey(Couple, on_delete=models.CASCADE, verbose_name="NS couple", related_name="ns_results")
    ew_couple = models.ForeignKey(Couple, on_delete=models.CASCADE, verbose_name="EW couple", related_name="ew_results")
    score = models.IntegerField(help_text="Positive for NS, negative for EW")
    
    class Meta:
        ordering = ('board',)
        unique_together = [('board', 'ns_couple'), ('board', 'ew_couple')]
    
    
    def couples(self):
        return (self.ns_couple, self.ew_couple)
    
    
    def ns_imps(self):
        """
        Return imps of the NS couple.
        """
        total_imps = sum(score_to_imps(self.score-r.score) for r in self.board.result_set.all())
        normalized_imps = float(total_imps) / (self.board.result_set.count() - 1) if self.board.result_set.count() > 1 else 0.0
        return normalized_imps
    
    """
    def couples_imps(self):
        imps = Counter()
        
        couples = self.couples()
        for i in xrange(2):
            imps[couples[i]] = (-1)**i * self.ns_imps()
        
        return imps
    """
    
    def couple_imps(self, couple):
        """
        Return imps of a given couple.
        """
        if couple == self.ns_couple:
            return self.ns_imps()
        elif couple == self.ew_couple:
            return -self.ns_imps()
        else:
            return 0.0


