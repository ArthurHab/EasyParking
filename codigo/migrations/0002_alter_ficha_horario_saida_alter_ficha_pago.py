# Generated by Django 4.0.6 on 2022-07-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='horario_saida',
            field=models.DateField(null=True, verbose_name='Horário de Saída'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pago',
            field=models.BooleanField(default=False),
        ),
    ]
