from django.contrib import admin
from stats.models import StockingGoods, StockingLog

# Register your models here.
admin.site.register(StockingLog)
admin.site.register(StockingGoods)
