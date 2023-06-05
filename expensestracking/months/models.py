from django.db import models

from core.models import Transection


class Month(Transection):
    income = models.BooleanField(default=False)
    expenses = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)
    extra = models.BooleanField(default=False)

    def __str__(self):
        return self.name
