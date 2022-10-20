# Generated by Django 4.1.2 on 2022-10-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('possivel_venda', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Proprietario',
                'verbose_name_plural': 'Proprietarios',
                'ordering': ['id'],
            },
        ),
    ]
