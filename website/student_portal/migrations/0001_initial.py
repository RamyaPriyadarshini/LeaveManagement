# Generated by Django 2.0.5 on 2019-02-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=25)),
                ('regno', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]