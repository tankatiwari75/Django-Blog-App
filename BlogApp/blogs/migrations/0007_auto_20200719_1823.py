# Generated by Django 3.0.8 on 2020-07-19 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200719_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]