# Generated by Django 4.2.9 on 2024-01-25 09:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=8)),
                ('slug', models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10)])),
                ('slug', models.CharField(max_length=255)),
                ('description', models.CharField(default=None, max_length=2000)),
                ('telephone', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=2000)),
                ('rating', models.FloatField(default=None)),
                ('images', models.CharField(default=None)),
                ('address', models.CharField(max_length=2000)),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.subcategory')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
            },
        ),
    ]
