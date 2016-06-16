#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128,verbose_name="姓名",null=False,blank=False)
    numb = models.IntegerField(verbose_name="被艾特次数",blank=True,default=0)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return self.name

class Expression(models.Model):
    text = models.CharField(max_length=280,verbose_name="文本内容",blank=True)
    pub_time = models.DateTimeField(verbose_name="发表时间",auto_now_add=True,blank=True)
    towhom = models.ForeignKey(Person,verbose_name="被表白者",null=False,blank=False)
    fromwhom = models.ForeignKey(Person,verbose_name="表白者",null=False,blank=False,related_name="fromwhom")

    class Meta:
        ordering = ['-pub_time']

    def __unicode__(self):
        return '%s to %s' % (self.fromwhom.name,self.towhom.name)