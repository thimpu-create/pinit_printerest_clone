from django.db import models
from django.contrib.auth.models import User
from . managers import UserManager
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='profiles/default.png', upload_to='profiles')
    about = models.TextField()
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    pronouns = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.user} is following {self.following}'