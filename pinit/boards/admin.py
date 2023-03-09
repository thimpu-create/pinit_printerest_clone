from django.contrib import admin

# Register your models here.
from . models import Board

class BoardMember(admin.ModelAdmin):
    list_display = ('User','title','cover','is_private','description')

admin.site.register(Board,BoardMember)