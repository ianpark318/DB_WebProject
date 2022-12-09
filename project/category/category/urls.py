"""category URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.display, name='index'),
    path('pc/', views.pc_inputData, name='index'),
    path('printer/', views.printer_inputData, name='index'),
    path('laptop/', views.laptop_inputData, name='index'),
    path('query1/', views.display_q1, name='query1'),
    path('query2/', views.display_q2, name='query2'),
    path('query3/', views.display_q3, name='query3'),
    path('query4/', views.display_q4, name='query4'),

]

