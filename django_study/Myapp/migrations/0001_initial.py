# Generated by Django 3.0.4 on 2020-03-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=6)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]