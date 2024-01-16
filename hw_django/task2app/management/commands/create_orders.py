from django.core.management.base import BaseCommand
from task2app.models import Order, Good, Client


class Command(BaseCommand):
    help = "Create orders."

    def handle(self , *args , **kwargs):
        good1 = Good.objects.filter(pk=9).first()
        good2 = Good.objects.filter(pk=10).first()
        good3 = Good.objects.filter(pk=11).first()
        good4 = Good.objects.filter(pk=12).first()
        client = Client.objects.filter(pk=1).first()
        order = Order(client=client, total=100.00)
        order.save()
        order.goods.add(good1, good2, good3, good4)
        self.stdout.write(f'Заказы составлены.')