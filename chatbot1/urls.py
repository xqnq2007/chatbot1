"""chatbot1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from bot1.views import index
import settings
#import bot1
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$',index,name='index'),
    url(r'^blog/',include('blog.urls')),
    url(r'^bot1/', include('bot1.urls')),
    url(r'^botinterface/',include('botinterface.urls'))
    #url(r'^static/(?P<path>.*)$',{'document_root': settings.STATIC_ROOT })
]
