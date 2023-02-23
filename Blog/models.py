from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 100, verbose_name = 'Заголовок')
    text = models.TextField(verbose_name = "Описане")
    author = models.CharField(max_length = 30, verbose_name = 'Автор')
    slug = models.CharField(max_length = 300, verbose_name = 'Категории') 
    timeStamp = models.DateTimeField(default = datetime.now, blank = True, 
                verbose_name = 'Дата публикации')

    def __str__(self):
        return self.title


class BlogComment(models.Model): 
    sno = models.AutoField(primary_key = True) 
    comment = models.TextField(verbose_name = 'Комментарии') 
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Пользователь') 
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Пост') 
    parent = models.ForeignKey('self', null = True, blank = True, on_delete = models.CASCADE, verbose_name = 'Родитель') 
    timeStamp = models.DateTimeField(default = now, verbose_name = 'Дата публикации') 

    def __str__(self): 
        return f'{self.comment[:13]}... by {self.user}' 

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

