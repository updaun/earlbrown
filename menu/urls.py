from django.urls import path
from .views import MenuCreateView, MenuListView, MenuDetailView, MenuUpdateView
from .apis import MenuCreateAPI, MenuDetailAPI, MenuUpdateAPI, MenuDeleteAPI
from .apis import MenuImageCreateAPI

app_name = "menu"

urlpatterns = [
    # VIEW
    path("create/", MenuCreateView.as_view(), name="create"),
    path("list/", MenuListView.as_view(), name="list"),
    path("detail/<int:pk>", MenuDetailView.as_view(), name="detail"),
    path("update/<int:pk>", MenuUpdateView.as_view(), name="update"),
    # API
    path("api/create/", MenuCreateAPI.as_view(), name="create-api"),
    path("api/detail/<int:pk>", MenuDetailAPI.as_view(), name="detail-api"),
    path("api/update/<int:pk>", MenuUpdateAPI.as_view(), name="update-api"),
    path("api/delete/<int:pk>", MenuDeleteAPI.as_view(), name="delete-api"),
    path(
        "api/image/create/<int:pk>",
        MenuImageCreateAPI.as_view(),
        name="image-create-api",
    ),
]
