# Generated by Django 4.2 on 2024-06-07 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0017_paymenttransaction_remove_paymentmethod_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, verbose_name='Número de Tarjeta')),
                ('expiration_date', models.DateField(verbose_name='Fecha de Expiración')),
                ('security_code', models.CharField(max_length=4, verbose_name='Código de Seguridad')),
                ('cardholder_name', models.CharField(default='', max_length=100, verbose_name='Nombre del Titular')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Metodo Pago')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=True, verbose_name='Activo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Metodo de Pago',
                'verbose_name_plural': 'Metodo de Pagos',
                'ordering': ['description'],
            },
        ),
        migrations.DeleteModel(
            name='PaymentTransaction',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='payment_method',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='credit_card', to='core.paymentmethod'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_method',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='payment_invoices', to='core.paymentmethod', verbose_name='Metodo pago'),
            preserve_default=False,
        ),
    ]
