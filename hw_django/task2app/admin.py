from django.contrib import admin
from .models import Client, Good, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']

class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'price', 'count']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client']
    ordering = ['id']
    list_filter = ['date']

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Order, OrderAdmin)