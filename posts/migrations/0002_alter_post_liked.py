# Generated by Django 3.2.18 on 2023-04-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profiles.Profile'),
        ),
    ]
