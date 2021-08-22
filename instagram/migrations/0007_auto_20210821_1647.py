# Generated by Django 3.2.5 on 2021-08-21 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20210821_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 21, 7, 47, 19, 326452, tzinfo=utc), null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]