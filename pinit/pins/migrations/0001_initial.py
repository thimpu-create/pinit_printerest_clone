# Generated by Django 4.1.7 on 2023-02-27 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pins')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='boards.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('pins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pins.pin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
