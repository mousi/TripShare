from django.conf.urls import patterns, url
from TripShare import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^post/$', views.addTrip, name='post'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r'^view/(?P<username>[\w\-]+)/$', views.view_profile, name='view_profile'),
    url(r'^join_trip/$', views.join_trip, name='join_trip'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^get_requests/$', views.get_requests, name='get_requests'),
    )
