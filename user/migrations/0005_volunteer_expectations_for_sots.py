# Generated by Django 4.2 on 2023-07-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='expectations_for_SOTS',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]