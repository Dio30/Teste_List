# Generated by Django 4.1.2 on 2022-10-18 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='proprietarios',
            field=models.ForeignKey(limit_choices_to={'cor': 3, 'modelos': 3}, on_delete=django.db.models.deletion.CASCADE, to='list.proprietarios'),
        ),
    ]
