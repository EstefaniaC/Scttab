from django.conf.urls import include, url
from apps.home.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'scttab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',index),
]
