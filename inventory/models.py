from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item (models.Model):
    title = models.CharField(max_length=200)  # need to specify max_length for this field type
    # title = models.CharField(max_length=200, null=True, blank=True) # ex filed attribute options
    description = models.TextField()
    amount = models.IntegerField()