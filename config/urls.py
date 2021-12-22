from django.contrib import admin
from django.urls import path, include

from moviedb.routers import router


urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
]
