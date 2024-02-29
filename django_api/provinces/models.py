from django.db import models
from django.utils.translation import gettext_lazy as _

class Provinces(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        TOTAL = 3, _('Total')
        UNKNOWN = 0, _('Unknown')

    province_name = models.CharField(max_length=255)
    gender = models.IntegerField(default=Gender.UNKNOWN, choices=Gender.choices)
    year = models.PositiveIntegerField()
    inhabitants = models.PositiveBigIntegerField()
