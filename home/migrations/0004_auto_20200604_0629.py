# Generated by Django 3.0.6 on 2020-06-04 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200604_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='courseName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Course'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
    ]
