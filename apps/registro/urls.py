from django.conf.urls import include, url
from apps.registro.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'scttab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',index),
    #url(r'^$',index2),
]