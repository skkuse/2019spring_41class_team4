# Generated by Django 2.2.1 on 2019-06-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]