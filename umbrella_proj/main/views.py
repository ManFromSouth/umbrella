from django.shortcuts import render
from .models import Good, SpecialOffer
from datetime import date


# Create your views here.
def home_view(request):
    # нужно считать данные из таблицы good, оформить в виде списка и передвть в окно
    response = list()
    # скидки и спецпредложения
    query = SpecialOffer.objects.all()
    for item in query:
        if (item.date_ends > date) & (item.date_begin < date):
            info = dict()
            info['type'] = 'offer'
            info['img'] = item.image
            response.append(info)
    # Товары
    query = Good.objects.filter(show=True)[:50]
    for item in query:
        info = dict()
        info['type'] = 'good'
        info['img'] = item.image_preview
        info['name'] = item.name
        info['price'] = item.price
        info['amount'] = item.amount
        info['reference'] = item.id
        response.append(info)

    return render(request, 'home.html', response)
