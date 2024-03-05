#from typing import Any
from django.http import HttpResponse
from blog.models import Author,Tags,Post,Comment
#from django.db.models import F
#from datetime import datetime


from django.views.generic import ListView


class AboutView(ListView):
    model = Author
    model = Tags
    model = Post
    model = Comment
    template_name = 'blog-full-width.html'


    def index(request):
        all = Author.objects.all()
        return HttpResponse(request, 'blog-full-width.html', {'object_list':all})