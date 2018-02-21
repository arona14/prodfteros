"""
Definition of urls for Fteros.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Fteros.views.home, name='home'),
    # url(r'^Fteros/', include('Fteros.Fteros.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/crm/', include('crm.api.urls', namespace='api-crm')),
    url(r'^api/gds/', include('gds.api.urls', namespace='api-gds')),
    url(r'^api/util/', include('util.api.urls', namespace='api-util')),
]
