# Generated by Django 3.0.3 on 2021-05-23 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210523_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
