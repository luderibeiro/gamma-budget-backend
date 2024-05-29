from budget.api.v1.views.revenue import *
from django.urls import include, path

urlpatterns: list[str] = [
    path("list/<int:user_id>/", RevenueListAPIView.as_view(), name="list"),
    path("create/<int:user_id>/", RevenueCreateAPIView.as_view(), name="create"),
    path("detail/<int:user_id>/<uuid:id>/", RevenueDetailAPIView.as_view(), name="detail"),
    path("update/<int:user_id>/<uuid:id>/", RevenueUpdateAPIView.as_view(), name="update"),
    path("delete/<int:user_id>/<uuid:id>/", RevenueDeleteAPIView.as_view(), name="delete"),
    # uuid: revenue_id
]
