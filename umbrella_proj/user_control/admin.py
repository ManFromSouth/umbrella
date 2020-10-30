from django.contrib import admin
from user_control.models import SiteUser, UserPhones, UserAddresses

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(UserPhones)
admin.site.register(UserAddresses)
