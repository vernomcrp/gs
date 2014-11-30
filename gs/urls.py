from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/vehicles/$', 'vehicle.views.vehicle_list'),
    url(r'^api/drive_historys/$', 'drive_history.views.drive_history_list')
)
