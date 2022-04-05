# Generated by Django 3.2.9 on 2022-04-01 01:46

import blogs.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EditSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Software', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Blogging',
            fields=[
                ('id', models.BigAutoField(default=blogs.models.create_id, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('images', models.ImageField(blank=True, upload_to='media/blog_uploads/')),
                ('video', models.FileField(blank=True, upload_to='')),
                ('embed_video_url', embed_video.fields.EmbedVideoField(blank=True, verbose_name='Youtube Video')),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='media/photos/')),
                ('caption', models.CharField(blank=True, max_length=80)),
                ('lens_type', models.CharField(blank=True, max_length=30)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogs.category')),
                ('edit_software', models.ManyToManyField(blank=True, related_name='software', to='blogs.EditSoftware')),
            ],
        ),
    ]