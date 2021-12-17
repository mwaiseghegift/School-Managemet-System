# Generated by Django 3.2.3 on 2021-12-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0004_indexevent400412'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexWhyUs700493',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='images/utils/%Y/%m')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
