from django.contrib import admin
from TripShare.models import User, UserProfile, Trip, TripUsers, Ratings, Requests

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(TripUsers)
admin.site.register(Trip)
admin.site.register(Ratings)
admin.site.register(Requests)