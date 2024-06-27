from budget.api.v1.views.limit import (
    LimitCreateAPIView,
    LimitDeleteAPIView,
    LimitListAPIView,
    LimitUpdateAPIView,
)
from django.urls import path

urlpatterns: list[str] = [
    path("list/<int:user_id>/", LimitListAPIView.as_view(), name="list"),
    path("create/<int:user_id>/", LimitCreateAPIView.as_view(), name="create"),
    path("update/<int:user_id>/<uuid:id>/", LimitUpdateAPIView.as_view(), name="update"),
    path("delete/<int:user_id>/<uuid:id>/", LimitDeleteAPIView.as_view(), name="delete"),
    # uuid: limit_id
]
