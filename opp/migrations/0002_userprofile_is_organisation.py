# Generated by Django 2.2.2 on 2020-07-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_Organisation',
            field=models.BooleanField(default=False),
        ),
    ]
