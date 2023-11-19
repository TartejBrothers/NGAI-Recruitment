from django.contrib import admin
from django.urls import path
from form import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.home, name="Home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
