# Generated by Django 2.2.6 on 2020-03-13 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200225_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='price',
        ),
    ]
