from django.core.management.base import BaseCommand
from task2app.models import Good


class Command(BaseCommand):
    help = "Create goods."

    def handle(self , *args , **kwargs):
        good1 = Good(name='Соль', describe='продукты питания', price=10.00, count=10)
        good1.save()
        good2 = Good(name='Сахар', describe='продукты питания', price=50.00, count=10)
        good2.save()
        good3 = Good(name='Мука', describe='продукты питания', price=40.00, count=10)
        good3.save()
        good4 = Good(name='Свинина', describe='продукты питания', price=500.00, count=10)
        good4.save()
        good5 = Good(name='Ростительное масло', describe='продукты питания', price=100.00, count=10)
        good5.save()
        good6 = Good(name='Рыба', describe='продукты питания', price=350.00, count=10)
        good6.save()
        self.stdout.write(f'Товары добавлены')