# Generated by Django 4.2.10 on 2024-05-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_permission_userpermission_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpermission',
            name='basis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.basis'),
        ),
    ]
