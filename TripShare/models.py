from django.contrib.auth.models import User
from django.db import models
import datetime

# Profile of Users. Users can have a driving licence, a car, number of ratings and averageRating.
# Used to add additional fields to the default Django User model.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes
    # Is this user a driver?
    isDriver = models.BooleanField(default=False)
    # Avatar (image)

    avatar = models.ImageField(upload_to='avatars', default='avatars/default.jpg') #TODO: https://github.com/matthewwithanm/django-imagekit

    # Date of birth
    dob = models.DateField()

    def __unicode__(self):
        return self.user.username

# Stores information about a specific Trip.
class Trip(models.Model):
    #description
    desc = models.CharField(max_length=255)
    #Trip creator
    creator = models.ForeignKey(User, related_name='creator')
    # From
    source = models.CharField(max_length=30)
    # To
    destination = models.CharField(max_length=30)
    #passenger_number
    pass_num = models.IntegerField()
    cost = models.FloatField(null=True)
    #Date when trip starts
    tripdate = models.DateTimeField()
    #Date the trip is posted
    dateposted = models.DateTimeField(auto_now=True)
    #dateposted = models.DateTimeField(default= datetime.datetime.now())

    def __unicode__(self):
        return self.source + " to " + self.destination

# A user can rate another user with a rating.
class Rating(models.Model):
    userRater = models.ForeignKey(User, related_name='rating_user')
    userRated = models.ForeignKey(User, related_name='rated_user')
    rating = models.IntegerField()

    class Meta:
        unique_together = ('userRater', 'userRated')

#The requests that users make to join a trip.
class Request(models.Model):
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)
    reqAccepted = models.NullBooleanField(default=None)

    class Meta:
        unique_together = ('user', 'trip')

#The users that have been approved to join the trip + the creator of the trip.
class TripUser(models.Model):
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)

    class Meta:
        unique_together = ('user', 'trip')
