from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from . models import Profile, Follow

class ProfileMember(admin.ModelAdmin):
    list_display = ('id','user','photo','about','fname','lname','website')

class FollowMember(admin.ModelAdmin):
    list_display = ('user','following')

class UserMember(UserAdmin):
    list_display = ("id","username", "email", "first_name", "last_name", "is_staff")

admin.site.register(Profile,ProfileMember)
admin.site.register(Follow,FollowMember)
admin.site.unregister(User)
admin.site.register(User,UserMember)