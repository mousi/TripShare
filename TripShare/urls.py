from django.conf.urls import patterns, url
from TripShare import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^post/$', views.addTrip, name='post'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^view/(?P<username>[\w\-]+)/$', views.view_profile, name='view_profile'),
    url(r'^join_trip/$', views.join_trip, name='join_trip'),
    url(r'^requests/$', views.view_requests, name='view_requests'),
    url(r'^respond_request/$', views.respond_request, name='respond_request'),
    url(r'^rate/$', views.rate_user, name='rate'),
    url(r'^checknotif/$', views.check_notifications, name='check_notifications'),
    )
