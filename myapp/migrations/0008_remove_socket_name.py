# Generated by Django 4.2.10 on 2024-05-16 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_appservice_service_type_delete_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socket',
            name='name',
        ),
    ]
