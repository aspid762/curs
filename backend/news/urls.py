"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("", include('django.contrib.auth.urls')),      # auth
    path("", RedirectView.as_view(url='news', permanent=True)),      # default page
    
    #path("base", views.index),                          # base.html
    path("index", views.dash),                          # index.html template
    path("content", views.dash),                        # index.html template
    path("about", views.about,name="about"),            # index.html about
    path("contacts", views.contacts,name="contacts"),   # index.html contacts
    path("news", views.news,name="news"),               # index.html contacts

    path("login",       views.login_news,    name="login"),           # auth    
    path("register",    views.register, name="register"),       # index.html contacts
    path("reset",       views.reset,    name="reset"),             # index.html contacts
    path("profile",     views.profile,  name="profile"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


