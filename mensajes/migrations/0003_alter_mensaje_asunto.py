# Generated by Django 4.2 on 2024-09-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_mensaje_asunto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='asunto',
            field=models.CharField(default='Sin asunto', max_length=255),
        ),
    ]
