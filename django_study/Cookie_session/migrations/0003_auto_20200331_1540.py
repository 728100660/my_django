# Generated by Django 3.0.4 on 2020-03-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cookie_session', '0002_auto_20200331_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='token',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
