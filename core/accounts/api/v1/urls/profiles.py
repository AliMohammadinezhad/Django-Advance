from django.urls import path

from .. import views

urlpatterns = [
    path('me/', views.ProfileApiView.as_view(), name='profile'),
]

 