# Generated by Django 4.2.10 on 2024-06-28 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('reg_number', models.CharField(max_length=100)),
                ('basis_file', models.FileField(upload_to='basis_files/')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventor_number', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=100)),
                ('manager_ip', models.CharField(max_length=100)),
                ('responsible_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('service_type', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.IntegerField()),
                ('subject', models.CharField(choices=[('at', 'AT'), ('os', 'Os'), ('hardware', 'Hardware'), ('host', 'Host'), ('user', 'User'), ('backend', 'Backend'), ('database', 'DataBase'), ('frontend', 'Front')], max_length=50)),
                ('object_id', models.IntegerField()),
                ('object', models.CharField(choices=[('at', 'AT'), ('os', 'Os'), ('hardware', 'Hardware'), ('host', 'Host'), ('user', 'User'), ('backend', 'Backend'), ('database', 'DataBase'), ('frontend', 'Front')], max_length=50)),
                ('given_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateTimeField()),
                ('basis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.basis')),
                ('basis_given_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bases_given_by', to=settings.AUTH_USER_MODEL)),
                ('permission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.permissiontype')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_hardware', to='myapp.hardware')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_os', to='myapp.os')),
            ],
        ),
        migrations.AddField(
            model_name='hardware',
            name='responsible_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.user'),
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_host', to='myapp.host')),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_soft_service', to='myapp.service')),
            ],
        ),
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('db_model', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='database_host', to='myapp.host')),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='database_soft_service', to='myapp.service')),
            ],
        ),
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_host', to='myapp.host')),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_service_soft', to='myapp.service')),
            ],
        ),
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('os', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.os')),
            ],
        ),
        migrations.CreateModel(
            name='AT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('backend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='at_back', to='myapp.backend')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='at_database', to='myapp.database')),
                ('frontend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='at_frontend', to='myapp.frontend')),
            ],
        ),
    ]
