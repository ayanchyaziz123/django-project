# Generated by Django 3.0.6 on 2020-06-04 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postAuthor', models.CharField(max_length=200)),
                ('postId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('postTitle', models.CharField(max_length=200)),
                ('postTimeDate', models.DateTimeField(auto_now_add=True)),
                ('postText', models.TextField()),
                ('postImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category')),
            ],
        ),
    ]