from django.conf.urls.defaults import *
from django.contrib import admin

handler500 = 'djangotoolbox.errorviews.server_error'

admin.autodiscover()

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('sccms.urls')),
)
