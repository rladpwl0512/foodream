"""foodream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
import upload.views
import mileage.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',upload.views.upload, name = "upload"),
    path('form/<int:form_id>/', upload.views.detail , name= "detail"),
    path('create', upload.views.create, name= 'create'),
    path('mileage/<int:mileage_id>', mileage.views.content, name= "content"),
    path('mileage/<int:mileage_id>/donate', mileage.views.donate, name= "donate"),
    path('mileage/popup', mileage.views.popup, name = "popup"),

    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
