# Generated by Django 3.0.3 on 2021-05-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_cancel_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.CharField(choices=[('YES', 'YES'), ('MAYBE', 'MAYBE'), ('NO', 'NO')], max_length=200, null=True),
        ),
    ]
