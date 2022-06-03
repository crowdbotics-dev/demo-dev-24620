from django.conf import settings
from django.db import models


class XYz(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
    user = models.TextField(
        null=True,
        blank=True,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
