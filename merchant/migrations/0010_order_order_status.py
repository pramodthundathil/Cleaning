# Generated by Django 5.0.6 on 2025-03-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0009_order_payment_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='pending', max_length=20),
        ),
    ]
