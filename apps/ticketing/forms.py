import random
import string
from django import forms
from django.contrib.auth.models import User
from .models import Ticket, Comment


class CreateTicketForm(forms.ModelForm):
    ticket_subject = forms.CharField(max_length=100)
    ticket_body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Ticket
        fields = ['ticket_subject', 'ticket_body']

class CreateCommentForm(forms.ModelForm):
    comment_body = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['comment_body']