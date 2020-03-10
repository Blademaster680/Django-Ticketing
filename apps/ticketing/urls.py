from django.urls import path
from django.conf.urls import url, include
from .views import TicketCreateView, TicketListView, ticket_detail

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket-list'),
    path('create-ticket/', TicketCreateView.as_view(), name='create-ticket'),
    path('<int:pk>/', ticket_detail, name='ticket-detail'),
]