from django.conf.urls import include, url
from apps.productividad.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'scttab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',productividad),
    #url(r'^$',index2),
]