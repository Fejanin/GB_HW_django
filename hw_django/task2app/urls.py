from django.urls import path
from . import views


urlpatterns = [
    path('', views.order, name='order'),
    path('<int:client_id>/<int:days>/', views.client_orders, name='client_orders'),
    ]