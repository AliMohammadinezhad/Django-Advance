from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        return super().get_queryset().filter(status=True)
    

class PostDetailView(DetailView):    
    model = Post
    