from django.db import models


# Create your models here.
from hw_django.settings import MEDIA_ROOT


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)


class Good(models.Model):
    name = models.CharField(max_length=100)
    describe = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)
    img = models.ImageField(null=True, blank=True, upload_to=MEDIA_ROOT)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
