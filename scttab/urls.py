"""scttab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registroNuevo', include('apps.registro.urls', namespace="registro"), name='registro'),
    url(r'^consulta', include('apps.consulta.urls', namespace="consulta"), name='consulta'),
    url(r'^usuarios', include('apps.usuarios.urls', namespace="usuarios"), name='usuarios'),
    url(r'^home', include('apps.home.urls', namespace="home"), name="home"),
    url(r'^revisiones', include('apps.revisiones.urls', namespace="revisiones"), name="revisiones"),
    url(r'^productividad', include('apps.productividad.urls', namespace="productividad"), name="productividad"),
]
