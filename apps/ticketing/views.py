from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ticket
from .forms import CreateTicketForm


class TicketCreateView(CreateView):
    model = Ticket
    form_class = CreateTicketForm
    template_name = 'ticketing/create_ticket.html'

    def form_valid(self, form):
        form.instance.ticket_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.author:
            return True
        return False


class TicketDetailView(DetailView):
    model = Ticket


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticketing/ticket.html'

    # https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django
