# coding=utf-8

from django.contrib.auth.models import User
from django.db import models


STATUS = (
    ('0', u"未开始"),
    ('1', u"进行中"),
    ('2', u"已结束"),
    ('3', u"已删除"),
    ('4', u"未参加"),
    ('5', u"已参加")
)


class ActivityCreate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField(u"标题", max_length=20)
    summary = models.CharField(u"介绍", max_length=50)
    start_time = models.DateTimeField(u"开始时间")
    end_time = models.DateTimeField(u"结束时间")
    status = models.CharField(u"活动状态", max_length=1, choices=STATUS, default='0')
    created_time = models.DateTimeField(auto_now_add=True)


class ActivityJoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    is_creater = models.BooleanField(default=False)
    activity = models.ForeignKey(ActivityCreate, on_delete=models.SET_NULL)
    status = models.CharField(u"活动状态", max_length=1, choices=STATUS)
    created_time = models.DateTimeField(auto_now_add=True)
