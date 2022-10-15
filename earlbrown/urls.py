from django.contrib import admin
from django.urls import path, include

# from .views import HomeView
from menu.views import MenuListView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', HomeView.as_view(), name="main"),
    path("", MenuListView.as_view(), name="main"),
    path("menu/", include("menu.urls")),
]
