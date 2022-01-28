# Generated by Django 3.2 on 2021-12-28 00:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payout', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('deactivated', models.DateTimeField(blank=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=400000)),
                ('date_created', models.DateField(default=datetime.datetime.now)),
                ('time_created', models.TimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(default=datetime.datetime.now)),
                ('time_created', models.TimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_by', models.CharField(blank=True, max_length=200)),
                ('wallet', models.CharField(blank=True, max_length=50, verbose_name='wallet address')),
                ('referal_code', models.CharField(default='tvOWqV', max_length=6, unique=True)),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crypto.membership')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('subcription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto.subcription')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crypto.price'),
        ),
        migrations.AddField(
            model_name='membership',
            name='subcription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crypto.subcription'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcription', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.CharField(blank=True, max_length=40, null=True)),
                ('payout', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=False)),
                ('subcribed', models.DateTimeField(blank=True, null=True)),
                ('deactivate', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Histories',
            },
        ),
    ]