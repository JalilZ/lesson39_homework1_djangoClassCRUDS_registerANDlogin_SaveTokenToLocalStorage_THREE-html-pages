"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # in project we will use urls.py (from Project) only once

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),    # in project we will use urls.py (from Project) only once
]


#This code should only be used during development and not in production. In production, serving static and media files should be handled by a web server or a content delivery network (CDN)
from django.conf import settings                                                 # IMAGE upload - Django4Kids
from django.conf.urls.static import static                                       # IMAGE upload - Django4Kids
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # IMAGE upload - Django4Kids
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   # IMAGE upload - Django4Kids