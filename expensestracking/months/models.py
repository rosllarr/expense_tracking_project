from django.db import models

from core.models import Transection


class Month(Transection):
    income = models.BooleanField()
    expenses = models.BooleanField()


class Catalog(models.Model):
    entry = models.ForeignKey(Month, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
