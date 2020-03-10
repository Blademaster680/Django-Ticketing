from datetime import datetime
from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    ticket_subject = models.CharField(max_length=100)
    ticket_body = models.TextField()
    ticket_user = models.CharField(max_length=100)
    ticket_created = models.DateField(default=datetime.now())

    def __str__(self):
        return self.ticket_subject

    def get_absolute_url(self):
        return reverse('dashboard')
