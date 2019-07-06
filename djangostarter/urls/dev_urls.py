from django.contrib import admin
from django.urls import path

from .base_urls import urlpatterns

urlpatterns += [
    path('admin/', admin.site.urls),
]