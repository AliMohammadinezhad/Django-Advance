from django.urls import include, path


from .views import PostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("api/v1/", include("blog.api.v1.urls")),
]
