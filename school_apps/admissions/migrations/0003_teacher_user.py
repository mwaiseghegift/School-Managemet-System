# Generated by Django 3.2.3 on 2021-11-04 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admissions', '0002_alter_student_admission_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
            preserve_default=False,
        ),
    ]
