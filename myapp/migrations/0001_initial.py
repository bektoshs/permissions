# Generated by Django 4.2.10 on 2024-05-14 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerLaptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=255)),
                ('netbios_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=255, null=True)),
                ('specifications', models.TextField()),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.os')),
                ('responsible_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.user')),
            ],
        ),
    ]
