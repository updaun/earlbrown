from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', HomeView.as_view(), name="main"),
    path("", HomeView.as_view(), name="main"),
    path("about/", AboutView.as_view(), name="about"),
    path("menu/", include("menu.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
