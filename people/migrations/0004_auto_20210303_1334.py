# Generated by Django 3.0.7 on 2021-03-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_audio_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='audio',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='story',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
