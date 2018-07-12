# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Couple(models.Model):
    name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.name


class Board(models.Model):
    number = models.IntegerField()
    
    def __str__(self):
        return "Board %d" % self.name
    
    class Meta:
        ordering = ('name',)


class Result(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    ns_couple = models.ForeignKey(Couple, on_delete=models.CASCADE)
    ew_couple = models.ForeignKey(Couple, on_delete=models.CASCADE)
    score = models.IntegerField(help_text="Positive for NS, negative for EW")
    
    class Meta:
        ordering = ('board',)
        unique_together = [('board', 'ns_couple'), ('board', 'ew_couple')]