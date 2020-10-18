from django.db import models
from main.models import Goods, Orders


# Информация о товарах в каждом конкретном заказе
class OrderGoods(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    amount_ordered = models.IntegerField()
    local_price = models.FloatField()  # цена товара на момент оплаты
    total_cost = models.FloatField()  # общая стоимость товаров
