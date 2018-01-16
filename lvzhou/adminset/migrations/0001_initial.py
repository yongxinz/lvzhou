# Generated by Django 2.0 on 2018-01-16 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=15, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('0', '女'), ('1', '男')], default='', max_length=1, verbose_name='性别')),
                ('autograph', models.CharField(default='', max_length=50, verbose_name='签名')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
