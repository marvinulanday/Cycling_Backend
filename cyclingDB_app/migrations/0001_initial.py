# Generated by Django 3.0.4 on 2020-04-21 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('popularity', models.IntegerField()),
                ('num_stages', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('manager', models.CharField(max_length=70)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Country')),
            ],
        ),
        migrations.CreateModel(
            name='TeamRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Race')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('stage_number', models.IntegerField()),
                ('stage_km', models.IntegerField()),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Race')),
                ('specialty',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Cyclist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('birthdate', models.DateField()),
                ('popularity', models.IntegerField()),
                ('leader', models.BooleanField()),
                ('size', models.FloatField()),
                ('weight', models.FloatField()),
                ('mountain', models.IntegerField()),
                ('plain', models.IntegerField()),
                ('downhilling', models.IntegerField()),
                ('sprint', models.IntegerField()),
                ('resistance', models.IntegerField()),
                ('recuperation', models.IntegerField()),
                ('timetrial', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Country')),
                ('specialty',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Specialty')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cyclingDB_app.Team')),
            ],
        ),
    ]
