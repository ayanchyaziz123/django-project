# Generated by Django 3.0.6 on 2020-06-04 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200604_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='courseName',
        ),
    ]
