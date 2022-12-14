# Generated by Django 4.0.6 on 2022-07-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codigo', '0006_alter_config_desconto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='desconto',
            field=models.PositiveIntegerField(default=30, verbose_name='Desconto para Usuário Cadastrado'),
        ),
        migrations.AlterField(
            model_name='config',
            name='preco',
            field=models.FloatField(verbose_name='Preço por Hora'),
        ),
    ]
