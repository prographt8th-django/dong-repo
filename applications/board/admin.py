from django.contrib import admin

# Register your models here.
from applications.board.models import Notice, Post, Comment, Scrap

admin.site.register(Notice)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Scrap)





