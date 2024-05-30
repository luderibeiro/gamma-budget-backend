from django.urls import include, path

urlpatterns = [
    path(
        "incoming/",
        include("budget.api.v1.urls.incoming"),
        name="incoming",
    ),
]
