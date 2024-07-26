from django import urls
from django.urls import include, path
from django.views.generic import TemplateView


from . import views

app_name = 'blog'

urlpatterns = [
    # path("posts/", views.PostListView.as_view(), name="post-list")
    path("api/v1/", include('blog.api.v1.urls'))
]
