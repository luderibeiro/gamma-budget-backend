from django.urls import include, path

from core.api.v1.views import auth as auth_views
from core.api.v1.views import user as user_views

app_name = "core"

user_paths: list[str] = [
    path(
        "user/list",
        user_views.UserListAPIView.as_view(),
        name="user_list",
    ),
    path(
        "user/alter_password/<int:pk>/",
        user_views.UserAlterPasswordAPIView.as_view(),
        name="user_alter_password",
    ),
    path(
        "user/register",
        user_views.UserCreateAPIView.as_view(),
        name="user_register",
    ),
    path(
        "auth",
        auth_views.AuthView.as_view(),
        name="auth",
    ),
]

urlpatterns: list[str] = [
    path("v1/", include("core.api.urls.v1_urls"), name="v1"),
    *user_paths,
]
