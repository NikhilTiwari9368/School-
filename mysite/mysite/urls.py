"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('about/',views.about),
    path('contact/',views.contact),
    path('submitform/',views.submitform , name="submitform"),
    path('calculator/' , views.calculator),
    # path('saveEnquiry/',views.saveEnquiry , name="saveEnquiry"),
    path('evenodd/',views.evenodd),
    path('newsdata/<newsid>',views.newsDetails),
    path('sport/',views.sport),
    path('Libarary/',views.Libarary),
    path('interactive/',views.interactive),
    path('admission/',views.admission),
    path('mission',views.mission),
]
