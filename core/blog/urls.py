from django.urls import include, path



app_name = "blog"

urlpatterns = [
    # path("posts/", views.PostListView.as_view(), name="post-list")
    path("api/v1/", include("blog.api.v1.urls"))
]
