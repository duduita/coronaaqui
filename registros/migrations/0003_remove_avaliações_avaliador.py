# Generated by Django 3.0.8 on 2020-08-09 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_avaliações_avaliador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliações',
            name='avaliador',
        ),
    ]
