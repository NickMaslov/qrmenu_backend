# Generated by Django 3.2 on 2022-05-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='place',
            name='font',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
