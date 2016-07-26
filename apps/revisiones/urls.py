from django.conf.urls import include, url
from apps.revisiones.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'scttab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',revision),
    url(r'^$',revision_oficio),

]