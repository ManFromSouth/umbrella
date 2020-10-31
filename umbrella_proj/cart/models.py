from django.db import models
from main.models import Good, Order


# Информация о товарах в каждом конкретном заказе
class OrderGood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    amount_ordered = models.IntegerField()
    local_price = models.FloatField()  # цена товара на момент оплаты
    total_cost = models.FloatField()  # общая стоимость товаров
