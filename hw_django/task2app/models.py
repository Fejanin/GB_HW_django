from django.db import models

# Create your models here.
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


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
