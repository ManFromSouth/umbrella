from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# расширение таблицы пользователей
# если надо
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # соединение с оргинальной таблицы
    # TODO: в тестах проверять на соответствсие этого поля с данными из таблицы Orders
    has_opened_order = models.BooleanField(default=False)  # Для оптимизации


# Нужна для связи с клиентом, а также для добавления спсика использованных клиентом номеров при заказе
class UserPhones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()


# Для хранения использованных клиентом адрессов
class UserAddresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.CharField(max_length=511)


