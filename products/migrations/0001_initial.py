# Generated by Django 3.0.8 on 2020-09-15 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(default='Enter general description')),
                ('description_2', models.TextField(default='Add product origin description, history, other details...')),
                ('finca', models.CharField(blank=True, max_length=30, null=True)),
                ('roast_level', models.CharField(default='e.g. dark', max_length=30)),
                ('cupping_notes', models.CharField(blank=True, max_length=100, null=True)),
                ('retail_price', models.DecimalField(decimal_places=2, default=1.0, max_digits=5)),
                ('new_product', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, default=5.0, max_digits=3, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('weather_temperature', models.CharField(max_length=100)),
                ('precipitation', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=100)),
                ('altitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Tell us your comments about this product')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_images', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Region'),
        ),
    ]
