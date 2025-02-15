from django.urls import path
from accounts.views import login_view, signup_view

"""
URL configuration for AirQualityMonitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.template.context_processors import request
# from django.contrib import admin


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('' , login_view , name='home') ,
    path('signup/', signup_view, name='signup'),

]
