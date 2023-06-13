from django.db import models
from mimetypes import guess_type
from django.utils.html import escape
from django.contrib.auth.models import User
from boards.models import Board
from django.shortcuts import render,redirect,get_object_or_404


class Pin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='pin_user')
    board = models.ForeignKey(Board,on_delete=models.CASCADE, related_name='boards')
    file = models.FileField(upload_to='pins')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_type(self):
        file_type = guess_type(self.file.url, strict=True)[0]
        # file_type might be ('video/mp4', None) or ('image/jpeg..etc', None)
        if 'video' in file_type:
            return 'video'
        elif 'image' in file_type:
            return 'image'
        

class Comment(models.Model):
    pins = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name= 'comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='all_comments')
    text = models.CharField(max_length=255)
    has_viewed_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} says {self.text}'
    
class Like(models.Model):
    pin = models.ForeignKey(Pin ,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)