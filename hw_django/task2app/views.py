from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ImgForm
from .models import Client, Order, Good
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
import datetime

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
    client = get_object_or_404(Client , pk=client_id)
    orders = Order.objects.filter(client=client, date__gte=period).order_by('-date')
    data = {
        'client': client.name,
        'goods': set(),
        'orders': orders,
    }
    for order in orders:
        for good in order.goods.all():
            data['goods'].add(good.name)
    return render(request, "task2app/client_orders.html", context=data)


def upload_img(request, good_id):
    good = get_object_or_404(Good , pk=good_id)
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['img']
            fs = FileSystemStorage()
            name = create_name(image.name)
            fs.save(name, image)
            good = Good.objects.filter(pk=good_id).first()
            good.img = 'media/' + name
            good.save()
    else:
        form = ImgForm()
    return render(request, 'task2app/upload_image.html', {'form': form, 'good': good.name})


def create_name(name_file):
    now = '_' + str(datetime.datetime.now()) + '.'
    name_file = now.join(name_file.split('.'))
    print(name_file)
    return name_file
