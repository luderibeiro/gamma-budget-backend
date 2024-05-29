from budget.api.v1.views.incoming import *
from django.urls import include, path

urlpatterns: list[str] = [
    path("list/<int:user_id>/", IncomingListAPIView.as_view(), name="list"),
    path("create/<int:user_id>/", IncomingCreateAPIView.as_view(), name="create"),
    path("detail/<int:user_id>/<uuid:id>/", IncomingDetailAPIView.as_view(), name="detail"),
    path("update/<int:user_id>/<uuid:id>/", IncomingUpdateAPIView.as_view(), name="update"),
    path("delete/<int:user_id>/<uuid:id>/", IncomingDeleteAPIView.as_view(), name="delete"),
    # uuid: incoming_id
]