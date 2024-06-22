# Generated by Django 4.2 on 2024-06-07 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_cart_cartitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Artículo'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('F', 'Fact        ura'), ('A', 'Anulada'), ('D', 'Devolucion')], default='F', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Artículo'),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16, verbose_name='Número de Tarjeta')),
                ('expiration_date', models.DateField(verbose_name='Fecha de Expiración')),
                ('security_code', models.CharField(max_length=4, verbose_name='Código de Seguridad')),
                ('cardholder_name', models.CharField(max_length=100, verbose_name='Nombre del Titular')),
                ('payment_method', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='credit_card', to='core.paymentmethod')),
            ],
            options={
                'verbose_name': 'Tarjeta de Crédito',
                'verbose_name_plural': 'Tarjetas de Crédito',
            },
        ),
    ]