# Generated by Django 4.2.10 on 2024-05-22 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_rename_user_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]