# Generated by Django 4.1.2 on 2022-10-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_proprietarios_possivel_venda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='proprietarios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proprietarios', related_query_name='proprietarios', to='list.proprietarios', verbose_name='Proprietário'),
        ),
        migrations.AlterField(
            model_name='proprietarios',
            name='possivel_venda',
            field=models.BooleanField(default=False),
        ),
    ]
