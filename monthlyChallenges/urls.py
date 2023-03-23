from django.contrib import admin
from django.urls import path, include

from challenges import views

urlpatterns = [
    path("", views.index),
    path('admin/', admin.site.urls),
    path("challenge/", include("challenges.urls"))
]
