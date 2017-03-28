from django.conf.urls.defaults import include, url
from flexselect import urls as flexselect_urls


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'tests.views.home', name='home'),
    # url(r'^tests/', include('tests.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flexselect/', include(flexselect_urls)),
]
