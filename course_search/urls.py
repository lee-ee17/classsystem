"""
URL configuration for course_search project.

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
from courses.views import index
from userauth.views import login_view, register_view, in_view, logout_view

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('courses/',  include('courses.urls')),      # 課程查詢
    path('recommend/',include('recommend.urls')),    # 人格測驗
    path('',          index,       name='index_html'),
    path('login/',    login_view,   name='login'),
    path('logout/',   logout_view,  name='logout'),
    path('register/', register_view,name='register'),
    path('in/',       in_view,      name='in'),
]
