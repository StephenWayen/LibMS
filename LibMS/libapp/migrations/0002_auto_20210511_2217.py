# Generated by Django 3.2 on 2021-05-11 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookslips',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
