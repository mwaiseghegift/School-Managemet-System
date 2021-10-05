# Generated by Django 3.2.3 on 2021-10-04 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(blank=True, max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('adm_timestamp', models.DateTimeField(auto_now_add=True)),
                ('has_cleared', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('adress', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='admissions.student')),
            ],
        ),
    ]