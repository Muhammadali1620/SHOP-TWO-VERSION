# Generated by Django 5.0.3 on 2024-04-20 11:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering_number', models.PositiveSmallIntegerField(unique=True)),
                ('name_uz', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('name_ru', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.maincategory')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_uz', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('value_ru', models.CharField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='features.feature')),
            ],
            options={
                'unique_together': {('feature', 'value_uz')},
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feature_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='features.featurevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.product')),
            ],
        ),
    ]
