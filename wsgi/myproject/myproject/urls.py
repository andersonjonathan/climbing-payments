from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^payments/', include('payments.urls', namespace="payments")),
    url(r'^', include('payments.urls', namespace="payments")),
    url(r'^admin/', include(admin.site.urls)),
)
