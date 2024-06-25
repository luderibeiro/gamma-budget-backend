from budget.api.v1.views.alert import (
    AlertCreateAPIView,
    AlertDeleteAPIView,
    AlertListAPIView,
    AlertUpdateAPIView,
)
from django.urls import path

urlpatterns: list[str] = [
    path("list/<int:user_id>/", AlertListAPIView.as_view(), name="list"),
    path("create/<int:user_id>/", AlertCreateAPIView.as_view(), name="create"),
    path("update/<int:user_id>/<uuid:id>/", AlertUpdateAPIView.as_view(), name="update"),
    path("delete/<int:user_id>/<uuid:id>/", AlertDeleteAPIView.as_view(), name="delete"),
    # uuid: alert_id
]
