"""starbucks URL Configuration

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
from django.conf.urls import url
from django.views.generic.base import TemplateView
from starbucks import views

urlpatterns = [

    path('accounts/', include('accounts.urls')),  # 아인
    url(r"^$",  views.give_reviews, name="home"),  # 근웅
    # url(r"^$", TemplateView.as_view(template_name="index.html"), views.give_reviews,name="home"),
    path('admin/', admin.site.urls),
    path("membership/", include("membership.urls")),
    path('order/', include('order.urls'))
]
