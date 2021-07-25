"""amblora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pat.urls')),
    path('hospital/', include('hospital.urls',namespace='hospital')),
    path('admin/', admin.site.urls),
    path('src/',include('src.urls',namespace='src')),
    path('polls/',include('polls.urls',namespace='polls')),
    path('notifications/',include('notifications.urls',namespace='notifications')),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# MEDIA_URL is used to point to the base URL for user-generated content - uploaded images, files, that sort of thing. 
# STATIC_URL is used as the prefix for JavaScript, CSS, etc.