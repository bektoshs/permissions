# Generated by Django 4.2.10 on 2024-07-17 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_userpermission_object_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='object',
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='subject',
        ),
        migrations.AddField(
            model_name='atm',
            name='asset',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backend',
            name='asset',
            field=models.OneToOneField(default=5, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='database',
            name='asset',
            field=models.OneToOneField(default=6, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frontend',
            name='asset',
            field=models.OneToOneField(default=7, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hardware',
            name='asset',
            field=models.OneToOneField(default=8, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='asset',
            field=models.OneToOneField(default=9, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset'),
            preserve_default=False,
        ),
    ]
