from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("crudapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handle error 404
handler404 = "crudapp.views.page_not_found"
handler500 = "crudapp.views.page_not_found"
