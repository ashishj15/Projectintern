# Generated by Django 2.2.2 on 2020-07-18 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opp', '0004_auto_20200718_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunites',
            name='votes_total',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voteproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opp.Opportunites')),
            ],
        ),
    ]