from django.contrib import admin

# Register your models here.
from . models import Pin,Comment

class PinMember(admin.ModelAdmin):
    list_display = ('user','board','file','title','link','description','date_created')

class CommentMember(admin.ModelAdmin):
    list_display = ('pins','user','text','date_created')

admin.site.register(Pin,PinMember)
admin.site.register(Comment,CommentMember)