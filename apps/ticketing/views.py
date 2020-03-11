from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .models import Ticket
from .forms import CreateTicketForm, CreateCommentForm


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

def ticket_detail(request, pk):
    template_name = 'ticketing/ticket_detail.html'
    ticket = get_object_or_404(Ticket, ticket_id=pk)
    comments = ticket.comments
    new_comment = None

    # Comment Posted
    if request.method == 'POST':
        comment_form = CreateCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment Object but dont save to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current ticket to the comment
            new_comment.ticket_id = ticket
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CreateCommentForm

    context = {'ticket': ticket,
         'comments': comments,
         'new_comment': new_comment,
         'comment_form': comment_form}

    return render(request, 'ticketing/ticket_detail.html', context)


#class TicketDetailView(DetailView):
#    model = Ticket
#    template_name = 'ticketing/ticket_detail.html'
#
#    class CommentCreateVeiw(CreateView):
#        form_class = CreateCommentForm
#
#        def form_valid(self, form):
#            form.instance.ticket_user = self.request.user
#            return super().form_valid(form) */


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticketing/ticket.html'

    # https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django
    def get_queryset(self):
        # Original qs
        qs = super().get_queryset()
        # Filter by a variable captured from url, for example
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
