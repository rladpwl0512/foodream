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
<<<<<<< HEAD
from django.urls import path
import upload.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',upload.views.upload, name = "upload"),
    path('form/<int:form_id>/', upload.views.detail , name= "detail"),
    path('create', upload.views.create, name= 'create'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include
import social.views 
import myapp.views
import upload.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', social.views.signin, name="signin"),
    path('accounts/', include('allauth.urls')),
    path('home/', myapp.views.home, name="home"),
    path('upload/',upload.views.upload, name = "upload"),
    path('form/<int:form_id>/', upload.views.detail , name= "detail"),
    path('create', upload.views.create, name= 'create'),
    # path('accounts/kakao/login/callback/', myapp.views.home, name="kakao callback"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> c317e4ace1bc59cfb713fe65bde036c61c9d042d
