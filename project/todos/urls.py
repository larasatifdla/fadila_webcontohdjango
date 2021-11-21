from django.urls import path

from .views import index

urlpatterns = [
    path('hello_index', index, name='hello_index'),
    path('ini_url', index, name='ini_url'),
]