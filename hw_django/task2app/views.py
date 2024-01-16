from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Order, Good
from datetime import datetime, timedelta


PERIODS = [7, 30, 365]


# Create your views here.
def order(request):
    return HttpResponse('На этой странице будут отображаться заказы.')


def client_orders(request, client_id, days):
    if days not in PERIODS:
        return HttpResponse('''
        Период выбран не корректно. 
        Допустимые значения: 7, 30, 365''')
    period = datetime.now().date() - timedelta(days=days)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client , date__gte=period).order_by('-date')
    data = {
        'client': client.name,
        'goods': set(),
        'orders': orders,
    }
    for order in orders:
        for good in order.goods.all():
            data['goods'].add(good.name)
    return render(request, "task2app/client_orders.html", context=data)
