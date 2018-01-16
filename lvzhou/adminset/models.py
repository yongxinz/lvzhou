# coding=utf-8

from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('0', u"女"),
    ('1', u"男")
)


class Profile(models.Model):
    """
    个人信息
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    nickname = models.CharField(u'昵称', max_length=15)
    gender = models.CharField(u"性别", max_length=1, choices=GENDER, default='')
    autograph = models.CharField(u'签名', max_length=50, default='')
    created_time = models.DateTimeField(u"注册时间", auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.user.first_name
