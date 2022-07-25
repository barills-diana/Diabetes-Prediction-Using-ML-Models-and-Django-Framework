"""DiabetesPrediction URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views   # . specify current dir

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("predict/", views.predict),
    path("predict/result/", views.result),
    path("research/", views.research),
    path("research/home/", views.home),
    path("blog/", views.blog),
    path("contact/", views.contact),
    path("research/predict/", views.predict),
    path("research/blog/", views.blog),
    path("research/contact/", views.contact),
    path("blog/research/", views.research),
    path("blog/contact/", views.contact),
    path("blog/predict/", views.predict),
    path("contact/research/", views.research),
    path("contact/contact/", views.contact),
    path("contact/predict/", views.predict),
    path("contact/blog/", views.blog),
    path("predict/research/", views.research),
    path("predict/contact/", views.contact),
    path("predict/blog/", views.blog)

]
