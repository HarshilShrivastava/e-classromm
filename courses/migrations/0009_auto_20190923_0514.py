# Generated by Django 2.2.4 on 2019-09-23 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190923_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursename',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
