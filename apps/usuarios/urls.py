from django.conf.urls import url
from apps.usuarios.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'scttab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',login),

]
