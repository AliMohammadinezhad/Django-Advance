from django import urls
from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = 'blog'

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="post-list")
]
