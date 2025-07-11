from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boshqaruv/', admin.site.urls),
    path('',include('homepage.urls')),
]
