# Generated by Django 3.2.5 on 2021-11-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customermsg', '0002_auto_20211103_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='messages',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]