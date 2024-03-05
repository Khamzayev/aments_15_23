from django.contrib import admin
from blog.models import Author,Post,Comment,Tags

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comment)