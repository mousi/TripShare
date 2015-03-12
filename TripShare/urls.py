from django.conf.urls import patterns, url
from TripShare import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^test/$', views.test, name='test'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^post/$', views.post, name='post'),
    )