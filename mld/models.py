from django.db import models

# Create your models here.
from django.utils import timezone


class Targets(models.Model):
    """геолакационные точки пользователя"""
    description = models.CharField(max_length=200)
    created_dt = models.DateTimeField(auto_now=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    # точка для всех пользовтелей
    isprivate = models.BooleanField(default=False)

    def __str__(self):
        txt = self.description
        return txt

    class Meta:
        unique_together = ('longitude', 'latitude')
