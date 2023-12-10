# Generated by Django 5.0 on 2023-12-10 17:42

import colorfield.fields
import datetime
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtraData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameExtra', models.CharField(max_length=100)),
                ('contentExtra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(default='Tarea', max_length=100)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('taskState', models.IntegerField(choices=[(0, 'Por hacer'), (1, 'En proceso'), (2, 'Cancelada'), (3, 'Finalizada')], default=0)),
                ('periodicity', models.IntegerField(choices=[(0, 'No periodico'), (1, 'Diario'), (2, 'Semanal'), (3, 'Mensual'), (4, 'Anual')], default=0)),
                ('dueDate', models.DateField(default=datetime.datetime.today)),
                ('dueTime', models.TimeField(blank=True, default='00:00')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Task.category')),
            ],
        ),
    ]
