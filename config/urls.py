# myblog/myblog/urls.py

from django.contrib import admin
from django.urls import path
from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
]
