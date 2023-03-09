# Generated by Django 4.1.7 on 2023-03-01 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0004_alter_board_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
