from django.contrib import admin
from TripShare.models import User, UserProfile, Trip, TripUser, Rating, Request

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TripUser)
admin.site.register(Trip)
admin.site.register(Rating)
admin.site.register(Request)