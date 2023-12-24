# Generated by Django 4.2.1 on 2023-06-05 18:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(upload_to='profilepics')),
                ('image2', models.ImageField(upload_to='profilepics')),
                ('allowedUsage', models.IntegerField(default=1)),
                ('blocked', models.BooleanField(default=False)),
                ('email', models.CharField(default='', max_length=200)),
                ('mobile', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=60)),
                ('father_name', models.CharField(max_length=60)),
                ('mother_name', models.CharField(max_length=60)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=300)),
                ('contactno', models.IntegerField(default=1)),
                ('email', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=150)),
                ('datajoined', models.DateField(default=datetime.date.today)),
                ('admin', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.adminuser')),
                ('token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.accesstoken')),
            ],
        ),
        migrations.CreateModel(
            name='subadminuser',
            fields=[
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('blocked', models.BooleanField(default=False)),
                ('email', models.CharField(default='', max_length=200)),
                ('mobile', models.IntegerField(default=1)),
                ('admin', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.adminuser')),
            ],
        ),
        migrations.CreateModel(
            name='notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('publishedDate', models.DateField(auto_now_add=True)),
                ('greetdate', models.DateField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.adminuser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='adminnotify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('publishedDate', models.DateField(auto_now_add=True)),
                ('greetdate', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.adminuser')),
            ],
        ),
    ]
