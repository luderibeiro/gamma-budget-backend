from django.urls import path

from budget.api.v1.views.categories import IncomingCategoryListAPIView
from budget.api.v1.views.incoming import (
    IncomingCreateAPIView,
    IncomingDeleteAPIView,
    IncomingDetailAPIView,
    IncomingListAPIView,
    IncomingUpdateAPIView,
)
from django.urls import path

urlpatterns: list[str] = [
    path(
        "list-categories/",
        IncomingCategoryListAPIView.as_view(),
        name="list-categories",
    ),
    path("list/<int:user_id>/", IncomingListAPIView.as_view(), name="list"),
    path("create/<int:user_id>/", IncomingCreateAPIView.as_view(), name="create"),
    path(
        "detail/<int:user_id>/<uuid:id>/",
        IncomingDetailAPIView.as_view(),
        name="detail",
    ),
    path(
        "update/<int:user_id>/<uuid:id>/",
        IncomingUpdateAPIView.as_view(),
        name="update",
    ),
    path(
        "delete/<int:user_id>/<uuid:id>/",
        IncomingDeleteAPIView.as_view(),
        name="delete",
    ),
    # uuid: incoming_id
]
