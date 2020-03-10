# Generated by Django 3.0.4 on 2020-03-10 12:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0007_auto_20200310_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('comment_user', models.CharField(max_length=100)),
                ('comment_created', models.DateField(default=django.utils.timezone.now)),
                ('comment_ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.Ticket')),
            ],
        ),
    ]