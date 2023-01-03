from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.listView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    templante_name = 'index.html'
    paginate_by = 6
