# Generated by Django 3.1 on 2020-08-21 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200821_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
