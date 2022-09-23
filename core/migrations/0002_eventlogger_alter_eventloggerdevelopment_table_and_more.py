# Generated by Django 4.1.1 on 2022-09-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLoggerAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': '"analytics"."event_logger"',
                'managed': True,
            },
        ),
        migrations.AlterModelTable(
            name='eventloggerdevelopment',
            table='"development"."event_logger"',
        ),
        migrations.AlterModelTable(
            name='siteurl',
            table='"seo"."site_url"',
        ),
    ]