from main.views import IndexView

app_name = "main"

from django.urls import path, include

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    )
]
