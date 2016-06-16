from django.db import models
from items.reclass import photoAndthumbField
from django.db.models import permalink
# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=100,verbose_name='Title')
    desc=models.TextField(verbose_name='Description')
    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('items_detail',None,{'pk':self.id})

class Photo(models.Model):
    title=models.CharField(max_length=100,verbose_name='Title')
    intro=models.TextField(verbose_name='Introduction')
    item=models.ForeignKey(Item,verbose_name='Item')
    publish_date=models.DateTimeField(auto_now_add=True)
    photo=photoAndthumbField(upload_to='uploads',verbose_name='Photo')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photos_detail',None,{'pk':self.id})