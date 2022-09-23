# Generated by Django 4.1.1 on 2022-09-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventLoggerDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('processed', models.BooleanField()),
            ],
            options={
                'db_table': '"analytics"."event_logger"',
                'db_tablespace': 'analytics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(blank=True)),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'site_url',
                'managed': False,
            },
        ),
    ]
