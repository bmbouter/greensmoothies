from django.db import models
from django.utils.translation import ugettext as _

class DrinkRecord(models.Model):
    datetime = models.DateTimeField(_('Date and Time'), auto_now_add=True)
    lat = models.FloatField(_('Latitude'))
    lng = models.FloatField(_('Longitude'))
