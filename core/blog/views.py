from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().filter(status=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
