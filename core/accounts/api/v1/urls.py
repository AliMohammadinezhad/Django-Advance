from django.urls import path, include
# from rest_framework.authtoken.views import ObtainAuthToken

from . import views

app_name = 'api-v1'

urlpatterns = [
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
]

 