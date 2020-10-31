from django.db import models
from main.models import Good


class StockingLog(models.Model):
    restock_date = models.DateField()


class StockingGood(models.Model):
    restock = models.ForeignKey(StockingLog, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    amount_restocked = models.IntegerField()
