from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# расширение таблицы пользователей
# если надо
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # соединение с оргинальной таблицы


# Нужна для связи с клиентом, а также для добавления спсика использованных клиентом номеров при заказе
class UserPhones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(not_null=True)


class UserAddreses(models.Model):
    user = models
    user_email = models.EmailField(not_null=True)


