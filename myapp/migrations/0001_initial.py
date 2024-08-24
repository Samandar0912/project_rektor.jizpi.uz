# Generated by Django 5.1 on 2024-08-24 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Murojat turi')),
            ],
            options={
                'verbose_name': 'Murojat turi',
                'verbose_name_plural': 'Murojat turi',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genders', models.CharField(max_length=100, verbose_name='Jinsi nomi')),
            ],
            options={
                'verbose_name': 'Jins',
                'verbose_name_plural': 'Jinslar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(max_length=100, verbose_name='viloyat nomi')),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Familiya')),
                ('name', models.CharField(max_length=100, verbose_name='ism')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('tel_number', models.CharField(max_length=15, verbose_name='Tell raqam')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('topic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Murajatni qisqacha mazmuni')),
                ('body', models.TextField(blank=True, null=True)),
                ('application_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.applicationtype')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.gender')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.region')),
            ],
            options={
                'verbose_name': "So'rovlar",
                'verbose_name_plural': "So'rovlar",
                'ordering': ['-id'],
            },
        ),
    ]
