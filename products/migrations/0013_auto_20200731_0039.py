# Generated by Django 3.0.8 on 2020-07-31 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_goodimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_files', to='products.Good'),
        ),
    ]
