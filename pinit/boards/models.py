from django.db import models
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import User

class Board(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,related_name='board_user')
    title = models.CharField(max_length=255)
    pins = models.ManyToManyField('pins.Pin',related_name='pins', blank=True)
    cover = models.ImageField(upload_to='boards',default='boards/default.png')
    is_private = models.BooleanField(default=False)
    description = models.CharField(max_length=255,blank=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
