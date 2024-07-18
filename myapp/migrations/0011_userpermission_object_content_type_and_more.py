# Generated by Django 4.2.10 on 2024-07-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('myapp', '0010_alter_hardware_inventor_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpermission',
            name='object_content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='object_permissions', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='subject_content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subject_permissions', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='basis_given_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_permissions', to='myapp.user'),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='subject_id',
            field=models.PositiveIntegerField(),
        ),
    ]