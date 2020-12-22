from django.shortcuts import render
from .models import Good, SpecialOffer
from datetime import date


# Create your views here.
def home_view(request):
    # нужно считать данные из таблицы good, оформить в виде списка и передвть в окно
    # скидки и спецпредложения
    query = SpecialOffer.objects.all()
    offers = list()
    for item in query:
        if (item.date_ends > date) & (item.date_begin < date):
            info = dict()
            info['img'] = item.image
            info['reference'] = item.reference
            offers.append(info)
    # Товары
    query = Good.objects.filter()[:50]
    goods = list()
    for item in query:
        info = dict()
        info['img'] = item.image_preview
        info['name'] = item.name
        info['price'] = item.price
        info['amount'] = item.amount
        info['reference'] = item.id
        goods.append(info)
    print(goods)
    return render(request, 'home.html', {'goods': goods, 'offers': offers})


def good_view(request, id_good):
    good = dict()
    item = Good.objects.get(id=id_good)
    good['image'] = item.image
    good['name'] = item.name
    good['price'] = item.price
    good['producer'] = item.producer
    good['info'] = item.info
    good['amount'] = item.amount
    return render(request, 'good_view.html', good)
