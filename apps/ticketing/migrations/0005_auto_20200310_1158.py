# Generated by Django 3.0.4 on 2020-03-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0004_auto_20200310_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(max_length=100),
        ),
    ]
