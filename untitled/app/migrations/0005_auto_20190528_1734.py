# Generated by Django 2.2.1 on 2019-05-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190528_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
