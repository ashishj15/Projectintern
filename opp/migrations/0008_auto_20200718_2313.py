# Generated by Django 2.2.2 on 2020-07-18 17:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opp', '0007_auto_20200718_2312'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'opportunites')},
        ),
    ]