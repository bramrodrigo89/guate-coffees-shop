# Generated by Django 3.0.8 on 2020-07-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='altitute',
            new_name='altitude',
        ),
    ]