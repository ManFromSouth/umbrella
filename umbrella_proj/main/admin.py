from django.contrib import admin
from main.models import Discounts, Perfume, Goods, Orders, SpecialOffers

# Register your models here.
admin.site.register(Goods)
admin.site.register(Perfume)
admin.site.register(Orders)
admin.site.register(SpecialOffers)
admin.site.register(Discounts)

