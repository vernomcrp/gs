from django.conf.urls import patterns, include, url
from django.contrib import admin


from rest_framework import routers
from drive_history import views

router = routers.DefaultRouter()

router.register('driver_history', views.DriveHistoryViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/vehicles/$', 'vehicle.views.vehicle_list')
)
