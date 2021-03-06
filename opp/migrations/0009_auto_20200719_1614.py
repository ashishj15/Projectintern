# Generated by Django 2.2.2 on 2020-07-19 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opp', '0008_auto_20200718_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='opportunites',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='opportunites',
            name='votes_total',
        ),
        migrations.AddField(
            model_name='opportunites',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'post', 'value')},
        ),
    ]
