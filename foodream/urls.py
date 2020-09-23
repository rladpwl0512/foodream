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
<<<<<<< HEAD
=======
import social.views 
import myapp.views
>>>>>>> 4aea679fcf1922e19eb5fb5001df706fb9724fdc
import upload.views
import mileage.views
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
<<<<<<< HEAD
    path('mileage/<int:mileage_id>', mileage.views.content, name= "content"),
    path('mileage/<int:mileage_id>/donate', mileage.views.donate, name= "donate"),
    path('mileage/popup', mileage.views.popup, name = "popup"),

    
=======
    path('list/', upload.views.list , name= "list"),
    # path('accounts/kakao/login/callback/', myapp.views.home, name="kakao callback"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 4aea679fcf1922e19eb5fb5001df706fb9724fdc

>>>>>>> c317e4ace1bc59cfb713fe65bde036c61c9d042d
