# Generated by Django 4.1.7 on 2023-03-13 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Марка авто')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('brand', models.CharField(max_length=50, verbose_name='Производитель')),
                ('artikul', models.TextField(blank=True, null=True, verbose_name='Номер')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='цена')),
                ('car_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop2.car_name')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop2.rubric')),
            ],
            options={
                'verbose_name': 'Запчасть',
                'verbose_name_plural': 'Запчасти',
                'ordering': ['id'],
            },
        ),
    ]
