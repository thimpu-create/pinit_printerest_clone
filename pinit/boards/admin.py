from django.contrib import admin

# Register your models here.
from . models import Board

class BoardMember(admin.ModelAdmin):
    list_display = ('id','User','title','cover','is_private','description','date_created')

admin.site.register(Board,BoardMember)