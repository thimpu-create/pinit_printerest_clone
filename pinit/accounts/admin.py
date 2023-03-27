from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from . models import Profile, Follow

class ProfileMember(admin.ModelAdmin):
    list_display = ('user','photo','about','fname','lname','website')

class FollowMember(admin.ModelAdmin):
    list_display = ('user','following')

admin.site.register(Profile,ProfileMember)
admin.site.register(Follow,FollowMember)