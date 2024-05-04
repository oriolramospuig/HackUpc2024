# Generated by Django 5.0.4 on 2024-05-04 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.city')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.event')),
            ],
        ),
        migrations.CreateModel(
            name='JourneyBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.business')),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.journey')),
            ],
        ),
        migrations.CreateModel(
            name='JourneyCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.city')),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.journey')),
            ],
        ),
        migrations.CreateModel(
            name='UserJourney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.journey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messi.user')),
            ],
        ),
    ]