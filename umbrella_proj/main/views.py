from django.shortcuts import render
from .models import Good, SpecialOffer


# Create your views here.
def home_view(request):
    # нужно считать данные из таблицы good, оформить в виде списка и передвть в окно
    response = list()
    # скидки и спецпредложения
    # TODO: Оставлять все что, имеет дату окончания выше текущей
    query = SpecialOffer.objects.all()
    for item in query:
        info = dict()
        info['type'] = 'offer'
        info['img'] = item.image
    # Товары
    # TODO: Фильтровать объекты по полю Show
    query = Good.objects.all()
    item_amount = 0
    for item in query:
        if item_amount >= 50:
            break
        info = dict()
        info['type'] = 'good'
        info['img'] = item.image_preview
        info['name'] = item.name
        info['price'] = item.price
        info['amount'] = item.amount
        info['reference'] = item.id
        response.append(info)
        item_amount += 1

    return render(request, 'home.html', response)
