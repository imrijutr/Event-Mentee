# Generated by Django 3.0.3 on 2021-05-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20210523_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.CharField(choices=[('YES', 'YES'), ('MAYBE', 'MAYBE'), ('NO', 'NO')], default='NO', max_length=200, null=True),
        ),
    ]