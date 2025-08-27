from django.db import models

class Metric(models.Model):
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    
