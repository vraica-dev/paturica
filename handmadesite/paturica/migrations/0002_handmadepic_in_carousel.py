# Generated by Django 4.2.5 on 2023-09-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paturica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='handmadepic',
            name='in_carousel',
            field=models.BooleanField(default=False),
        ),
    ]
