from django.urls import path
from django.contrib import admin
from accounts.views import login_view, signup_view, data_view, trends_view, home_view

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
#from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('home/' , home_view , name='home'),
    path('signup/', signup_view, name='signup'),
    path('data/', data_view, name = 'data'),
    path('trends/', trends_view, name = 'trends'),


]
