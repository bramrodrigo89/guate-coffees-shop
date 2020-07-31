# Generated by Django 3.0.8 on 2020-07-31 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200730_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='finca',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='roast_level',
            field=models.CharField(default='some text', max_length=30),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.TextField(default='some text'),
        ),
        migrations.AlterField(
            model_name='good',
            name='description_2',
            field=models.TextField(default='some text'),
        ),
    ]