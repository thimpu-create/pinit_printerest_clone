# Generated by Django 4.1.7 on 2023-05-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='has_viewed_status',
            field=models.BooleanField(default=False),
        ),
    ]
