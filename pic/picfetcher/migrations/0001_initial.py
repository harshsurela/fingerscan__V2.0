# Generated by Django 4.2.1 on 2023-06-05 18:52

from django.db import migrations, models
import django.db.models.deletion
import picfetcher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=picfetcher.models.PathAndRename('pics'))),
                ('name', models.CharField(default='', max_length=70)),
                ('camera_selected', models.CharField(default='False', max_length=6)),
                ('publishedDate', models.DateField(auto_now_add=True)),
                ('processedimg', models.ImageField(upload_to=picfetcher.models.PathAndRename('pics'))),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
