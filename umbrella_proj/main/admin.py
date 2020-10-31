from django.contrib import admin
from main.models import Discount, Perfume, Good, Order, SpecialOffer

# Register your models here.
admin.site.register(Good)
admin.site.register(Perfume)
admin.site.register(Order)
admin.site.register(SpecialOffer)
admin.site.register(Discount)

