from __future__ import unicode_literals
from django.db import models

class Enrolment(models.Model):
  unique_id = models.AutoField(primary_key=True)
  id = models.IntegerField(blank=True, null=True)
  dept = models.CharField(max_length=4, blank=True, null=True)
  number = models.IntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'enrolment'

class Similarity(models.Model):
  unique_id = models.AutoField(primary_key=True)
  from_class = models.FloatField()
  to_class = models.FloatField()
  score = models.FloatField()
    
  class Meta:
    managed = False
    db_table = 'similarity'