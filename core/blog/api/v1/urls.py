from rest_framework.routers import DefaultRouter


from . import views

app_name = "api-v1"


router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls


# urlpatterns = [
#     # path("", post_list, name="post_list"),
#     # path("<int:pk>/", views.post_detail, name="post_list"),
#     # path("", views.PostListView.as_view(), name="post_list"),
#     # path("<int:pk>/", views.PostDetailView.as_view(), name="post_list"),
#     # path("post/", views.PostViewSet.as_view({'get':'list'}), name="post"),
#     # path("post/<int:pk>", views.PostViewSet.as_view({'get':'retreive'}), name="post")
#     # path('', include(router.urls))
# ]
