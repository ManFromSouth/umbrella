from django.contrib import admin
from stats.models import StockingGood, StockingLog

# Register your models here.
admin.site.register(StockingLog)
admin.site.register(StockingGood)
