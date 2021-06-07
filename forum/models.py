from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 80, default = 'title missing')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length = 80, default = 'title missing')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete = models.PROTECT)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)

    def __str__(self):
        return self.title
