import re
from turtle import st
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='İstifadəçi Adı')
    title = models.CharField(max_length=150,verbose_name='Başlıq')
    content = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add = True , verbose_name ='Tarix' )
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    
    def __str__(self):
        return str(self.title)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Article,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default="Like",max_length=10)
    
    def __str__(self):
        return str(self.post)