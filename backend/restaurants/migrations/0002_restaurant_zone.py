# Generated by Django 3.0.7 on 2020-07-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='zone',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]