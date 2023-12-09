# Generated by Django 5.0 on 2023-12-09 02:21

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idCat', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtraData',
            fields=[
                ('idExtra', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nameExtra', models.CharField(max_length=100)),
                ('contentExtra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('idTask', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('taskState', models.IntegerField(choices=[(0, 'Por hacer'), (1, 'En proceso'), (2, 'Cancelada'), (3, 'Finalizada')], default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task.category')),
            ],
        ),
    ]
