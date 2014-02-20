from django.db import models

# Create your models here.        
class Menu(models.Model):
    name = models.CharField('Menu Name', max_length=50)
    class_name = models.CharField('Menu Class', max_length=50)
    def __unicode__(self):
        return self.name
    
class PagesContent(models.Model):
    name = models.CharField('Page Name', max_length=50)
    link = models.CharField('Page Link', max_length=50)
    menu = models.ForeignKey(Menu)
    content=models.TextField('Put content of page here')
    def __unicode__(self):
        return self.link
    
    class Meta:
        verbose_name_plural = "Pages Content"