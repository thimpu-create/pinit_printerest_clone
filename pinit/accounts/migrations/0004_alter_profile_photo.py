# Generated by Django 4.1.7 on 2023-02-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profiles/default.png', upload_to='profiles'),
        ),
    ]
