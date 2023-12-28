from django.core.management.base import BaseCommand
from task2app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self , *args , **kwargs):
        client = Client(name='John', email='john@example.com', phone='+7(999)999-99-99', address='Moscow')
        client.save()
        self.stdout.write(f'{client}')