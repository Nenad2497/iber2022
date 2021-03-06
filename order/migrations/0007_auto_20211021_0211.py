# Generated by Django 3.2.7 on 2021-10-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20211021_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Na čekanju', 'Na čekanju'), ('Prihvaćeno', 'Prihvaćeno'), ('Odbijeno', 'Odbijeno')], default='Na čekanju', max_length=200),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Na čekanju', 'Na čekanju'), ('Prihvaćeno', 'Prihvaćeno'), ('Odbijeno', 'Odbijeno')], default='Na čekanju', max_length=200),
        ),
    ]
