# Generated by Django 3.2 on 2021-05-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_auto_20210525_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='cip',
            name='clazz',
            field=models.CharField(choices=[('0', '马列毛邓'), ('1', '哲学'), ('2', '社会科学'), ('3', '自然科学'), ('4', '综合类'), ('5', '其他')], default='5', max_length=100, null=True, verbose_name='图书种类'),
        ),
        migrations.AddField(
            model_name='cip',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='封面'),
        ),
    ]
