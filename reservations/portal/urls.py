from django.contrib import admin
from django.urls import path

from .views import index, reserve

urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('reserve', reserve.Reserve.as_view(), name='reserve')
]