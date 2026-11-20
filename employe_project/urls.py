from django.contrib import admin
from django.urls import path,include

import employe

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('employe.urls')),

]