# Generated by Django 4.2.1 on 2023-06-15 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_admin_userprofile_bloodgroup_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='token',
        ),
    ]
