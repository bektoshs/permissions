# Generated by Django 4.2.10 on 2024-05-22 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_alter_computerlaptop_specifications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
