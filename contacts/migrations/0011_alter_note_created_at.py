# Generated by Django 3.2.4 on 2021-06-17 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_alter_note_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 17, 21, 9, 42, 33927, tzinfo=utc)),
        ),
    ]