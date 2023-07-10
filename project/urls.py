from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("dropbox/", include("apps.boxed_and_dropped.urls")),
    path("coffee/", include("apps.coffee_machine.urls")),
]
