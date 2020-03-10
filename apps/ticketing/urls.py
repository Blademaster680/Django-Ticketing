from django.urls import path
from django.conf.urls import url, include
from .views import TicketCreateView, TicketDetailView, TicketListView

urlpatterns = [
    path('', TicketListView.as_view(), name='ticket-list'),
    path('create-ticket/', TicketCreateView.as_view(), name='create-ticket'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]