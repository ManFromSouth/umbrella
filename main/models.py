from django.db import models
from user_control.models import *
from phonenumber_field.modelfields import PhoneNumberField


# Здесь хранится общая информация о заказах
class Orders(models.Model):
    # Выборы для choices
    FULFILLED = 'F'  # заказ оплачен и получен
    CANCELED = 'C'  # заказ оплачен и отменен
    PAYED = 'P'  # заказ оплачен и не получен
    RESERVED = 'R'  # заказ как либо зарезервирован
    OPENED = 'O'  # заказ открыт и неоплачен (в корзине)
    # ХЗ как сделать так, чтобы можно было прочитать но не изменить эти поля
    status_choices = [(FULFILLED, 'Получен'), (CANCELED, 'Отменен'), (PAYED, 'Оплачен'),
                      (RESERVED, 'Зарезервирован'), (OPENED, 'Открыт')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: Проработать choices
    payment_type = models.CharField(max_length=2)
    # TODO: в тестах проверять наличие всех адрессов для данного пользователя в таблице UserAddresses
    order_address = models.CharField(not_null=True, max_length=511)
    # TODO: в тестах проверять наличие всех адрессов для данного пользователя в таблице UserPhones
    order_phone_num = PhoneNumberField(not_null=True)
    order_status = models.CharField(not_null=True, max_length=1, choices=status_choices)
    order_cost = models.FloatField()
