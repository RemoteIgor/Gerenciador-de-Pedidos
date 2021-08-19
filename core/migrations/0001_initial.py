# Generated by Django 3.2.6 on 2021-08-18 23:25

import core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, null='True', validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Preço Unitário')),
                ('multiplo', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='multiplo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, null='True', validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Preço')),
                ('quantidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), core.models.validate_even], verbose_name='Quantidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto', validators=[core.models.retorna_produto])),
            ],
        ),
    ]
