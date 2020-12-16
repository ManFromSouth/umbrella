from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Здесь хранится общая информация о заказах
class Order(models.Model):
    # Выборы для choices
    FULFILLED = 'F'  # заказ оплачен и получен
    CANCELED = 'C'  # заказ оплачен и отменен
    PAYED = 'P'  # заказ оплачен и не получен
    RESERVED = 'R'  # заказ как либо зарезервирован
    OPENED = 'O'  # заказ открыт и неоплачен (в корзине)
    # ХЗ как сделать так, чтобы можно было прочитать, но не изменить эти поля
    status_choices = [(FULFILLED, 'Получен'), (CANCELED, 'Отменен'), (PAYED, 'Оплачен'),
                      (RESERVED, 'Зарезервирован'), (OPENED, 'Открыт')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: Проработать choices
    payment_type = models.CharField(max_length=2)
    # TODO: в тестах проверять наличие всех адрессов для данного пользователя в таблице UserAddresses
    order_address = models.CharField(max_length=512)
    # TODO: в тестах проверять наличие всех адрессов для данного пользователя в таблице UserPhones
    order_phone_num = PhoneNumberField()
    order_status = models.CharField(max_length=1, choices=status_choices)
    # поле вычисляется на основе OrderGoods
    order_cost = models.FloatField()
    # здесь проставливаются даты установления соответствующих состояний заказов
    date_reserved = models.DateField()
    date_payed = models.DateField()
    date_fulfilled = models.DateField()


class Good(models.Model):
    PERFUME = 'per'
    COSMETICS = 'cos'
    goods_types = [(PERFUME, 'Парфюм'), (COSMETICS, 'Косметика')]
    name = models.CharField(max_length=256)
    price = models.FloatField()
    producer = models.CharField(max_length=256)
    info = models.CharField(max_length=512)  # отображаемая инфа о товаре
    image = models.ImageField()  # большой вариант катринки товара
    image_preview = models.ImageField()  # малый вариант картинки товара, используемый в списках
    amount = models.IntegerField()  # количество товара на "складе"
    type = models.CharField(max_length=3, choices=goods_types)  # типы для поиска
    show = models.BooleanField()


# доп инфа для парфюма
class Perfume(models.Model):
    good = models.OneToOneField(Good, on_delete=models.CASCADE)
    aroma = models.CharField(max_length=256)


class SpecialOffer(models.Model):
    DISCOUNT = 'dis'
    offer_types = [(DISCOUNT, 'Скидка')]
    date_begin = models.DateField()  # Начало акции
    date_ends = models.DateField()  # Конец акции
    offer_image = models.ImageField()  # Изображение, показуемое на экране
    reference = models.CharField() # Ссылка для перехода
    type = models.CharField(max_length=3, choices=offer_types)


class Discount(models.Model):
    offer = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    amount = models.IntegerField()  # измеряется в процентах от оригинальной цены



