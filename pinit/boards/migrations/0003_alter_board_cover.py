# Generated by Django 4.1.7 on 2023-02-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='cover',
            field=models.ImageField(default='boards/default.png', upload_to='boards'),
        ),
    ]
