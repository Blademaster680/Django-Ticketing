from django.urls import path
from django.conf.urls import url, include
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]