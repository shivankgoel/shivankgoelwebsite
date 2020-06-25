"""cbprojects URL Configuration

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
from django.urls import path, include
from django.http import HttpResponse, HttpResponseRedirect



def read_file(request):
    f = open('.well-known/pki-validation/E51057ABC0998BDD1E63634DBD44DB0C.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('.well-known/pki-validation/E51057ABC0998BDD1E63634DBD44DB0C.txt', read_file),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('auth/', include('auth.urls')),
    path('', include('homepage.urls')),
]
