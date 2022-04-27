# Generated by Django 4.0.4 on 2022-04-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibuy', '0002_rename_nome_categoria_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.FileField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='produto',
            name='nome_imagem',
            field=models.CharField(default='', max_length=200),
        ),
    ]
