from budget.api.v1.views import user
from django.urls import include, path

app_name = "budget"

urlpatterns = [
    path(
        "v1/",
        include("budget.api.urls.v1_urls"),
        name="v1",
    ),
]
