# Generated by Django 3.0.7 on 2020-07-14 15:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200704_2225'),
        ('restaurants', '0008_auto_20200705_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodreview',
            name='text',
            field=models.TextField(blank=True, verbose_name='Food Review'),
        ),
        migrations.AddField(
            model_name='foodreview',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantreview',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantyoutubereview',
            name='priority',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='restaurantyoutubereview',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodreview',
            name='review',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='services.YoutubeReview'),
        ),
    ]