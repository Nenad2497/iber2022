# Generated by Django 3.2.5 on 2021-11-01 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20211021_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_baner',
        ),
    ]
