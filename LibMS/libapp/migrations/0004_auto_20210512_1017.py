# Generated by Django 3.2 on 2021-05-12 10:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0003_auto_20210511_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookslips',
            name='status',
            field=models.CharField(choices=[('0', '未完成'), ('1', '已完成'), ('2', '已通知')], default='未完成', max_length=5, verbose_name='当前状态'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='status',
            field=models.CharField(choices=[('0', '未完成'), ('1', '已完成'), ('2', '已通知')], default='未完成', max_length=5, verbose_name='预约状态'),
        ),
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='产生时间')),
                ('money', models.IntegerField(verbose_name='金额')),
                ('status', models.CharField(choices=[('0', '未完成'), ('1', '已完成'), ('2', '已通知')], default='未完成', max_length=5, verbose_name='支付状态')),
                ('borrow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.bookslips', verbose_name='关联的借阅记录')),
            ],
            options={
                'verbose_name': '罚金管理',
                'verbose_name_plural': '罚金管理',
            },
        ),
    ]
