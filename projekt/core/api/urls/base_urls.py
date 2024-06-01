from django.urls import include, path

from core.api.v1.views import auth as authViews
from core.api.v1.views import user as userViews

app_name = "core"

user_paths: list[str] = [
    path(
        "user/list",
        userViews.UserListAPIView.as_view(),
        name="user_list",
    ),
    path(
        "user/alter_password/<int:pk>/",
        userViews.UserAlterPasswordAPIView.as_view(),
        name="user_alter_password",
    ),
    path(
        "user/register",
        userViews.UserCreateAPIView.as_view(),
        name="user_register",
    ),
    path(
        "auth",
        authViews.AuthView.as_view(),
        name="auth",
    ),
]

urlpatterns: list[str] = [path("v1/", include("core.api.urls.v1_urls"), name="v1"), *user_paths]
