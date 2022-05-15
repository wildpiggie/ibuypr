# Generated by Django 4.0.4 on 2022-05-14 22:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibuy', '0014_historicocompras'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='historicocompras',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, validators=[django.core.validators.MaxValueValidator(9999.99), django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]