# Generated by Django 4.1.7 on 2023-02-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pins', '0001_initial'),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='pins',
            field=models.ManyToManyField(blank=True, related_name='pins', to='pins.pin'),
        ),
    ]
