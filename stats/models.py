from django.db import models
from main.models import Goods


class StockingLog(models.Model):
    restock_date = models.DateField()


class StockingGoods(models.Model):
    restock = models.ForeignKey(StockingLog, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    amount_restocked = models.IntegerField()