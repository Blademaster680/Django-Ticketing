from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import random


def random_string():
    return str(random.randint(100000, 999999))


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=100, default=random_string, primary_key=True)
    ticket_subject = models.CharField(max_length=100)
    ticket_body = models.TextField()
    ticket_user = models.CharField(max_length=100)
    ticket_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.ticket_subject

    def get_absolute_url(self):
        return reverse('ticket-detail', args=[self.ticket_id])




