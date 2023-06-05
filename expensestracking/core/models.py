from django.db import models


class Transection(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(null=True)
    due_date = models.DateField(null=True)

    class Meta:
        abstract = True
