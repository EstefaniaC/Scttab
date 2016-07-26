from django.conf.urls import url
from apps.consulta.views import index

urlpatterns = [
    url(r'^$', index),
]