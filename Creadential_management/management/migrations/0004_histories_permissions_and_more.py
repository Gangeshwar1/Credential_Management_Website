# Generated by Django 4.1.3 on 2022-11-22 05:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_website_credentials_alter_customuser_login_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='histories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Id', models.IntegerField()),
                ('login_date', models.DateField(auto_now_add=True)),
                ('login_time', models.TimeField()),
                ('login_ip_address', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField()),
                ('permission', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='login_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 22, 11, 3, 53, 700221)),
        ),
        migrations.AlterField(
            model_name='website_credentials',
            name='user_ids',
            field=models.CharField(max_length=100),
        ),
    ]