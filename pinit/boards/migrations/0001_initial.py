# Generated by Django 4.1.7 on 2023-02-27 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(default='static/default.png', upload_to='boards')),
                ('is_private', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
