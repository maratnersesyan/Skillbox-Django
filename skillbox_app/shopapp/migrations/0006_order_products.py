# Generated by Django 5.0.4 on 2024-04-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products', to='shopapp.product'),
        ),
    ]
