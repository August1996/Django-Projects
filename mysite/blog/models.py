# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
# Create your models here.
class User(AbstractUser):
	avatar = models.ImageField(upload_to = 'uploads/avatar/%Y/%m',default = 'uploads/avatar/default.png',max_length = 100,verbose_name = '用户头衔',blank = True,null = True)
	url = models.URLField(max_length = 48,verbose_name = '个人网站')
	intro = models.TextField(null = False,blank = False,verbose_name = '简介')
	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		ordering = ['-id']

	def __unicode__(self):
		return self.username

class Category(models.Model):
	name = models.CharField(max_length = 48,verbose_name = '分类名称')
	index = models.IntegerField(blank = True,null = True,default = 999,verbose_name = '分类索引')

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = verbose_name
		ordering = ['index','id']

	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 48,verbose_name = '标签')

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name


class Article(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length = 128,verbose_name = '标题')
	content = models.TextField(verbose_name = '正文')
	publish_time = models.DateTimeField(auto_now_add = True,verbose_name = '发表时间')
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag)
	click_num = models.IntegerField(blank =True,null = True,default = 0)
	is_recommend = models.BooleanField(blank = True,default = False,verbose_name = '是否推荐')

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = verbose_name
		ordering = ['-id']

	def __unicode__(self):
		return self.title

