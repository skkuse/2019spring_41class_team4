# Generated by Django 2.2.1 on 2019-06-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190604_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
