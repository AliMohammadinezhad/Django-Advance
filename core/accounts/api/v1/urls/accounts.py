from django.urls import path
from rest_framework_simplejwt import views as auth_views


from .. import views


urlpatterns = [
    # registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    # path('test-email/', views.TestEmailSend.as_view(), name='test-email'),
    # activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    # resend activation
    path(
        "activation/resend/",
        views.ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    # password change
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # login token
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),
    path(
        "logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"
    ),
    # login jwt
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="token-create",
    ),
    path(
        "jwt/refresh/",
        auth_views.TokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path(
        "jwt/verify/",
        auth_views.TokenVerifyView.as_view(),
        name="token-verify",
    ),
]
