from django.contrib import admin
from user_control.models import SiteUser, UserPhone, UserAddress

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(UserPhone)
admin.site.register(UserAddress)
