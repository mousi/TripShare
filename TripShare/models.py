from django.contrib.auth.models import User
from django.db import models

# Profile of Users. Users can have a driving licence, a car, number of ratings and averageRating.
# Used to add additional fields to the default Django User model.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes
    driver = models.BooleanField(default=False)
    hasCar = models.BooleanField(default=False)
    numRatings = models.IntegerField(default=0)
    # Avatar (image)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    #RatingSum ???
    avgRating = models.FloatField(null=True)

    def __unicode__(self):
        return self.user.username

# Stores information about a specific Trip.
class Trip(models.Model):
    #description
    desc = models.CharField(max_length=255)
    #Trip creator
    creator = models.ForeignKey(UserProfile, related_name='creator')
    # From
    source = models.CharField(max_length=30)
    # To
    destination = models.CharField(max_length=30)
    #passenger_number
    pass_num = models.IntegerField(default=0)
    datetime = models.DateTimeField()

    carOwner = models.ForeignKey(UserProfile, related_name='carOwner', null=True)

    def __unicode__(self):
        return self.desc

# A user can rate another user with a rating.
class Ratings(models.Model):
    userRater = models.ForeignKey(UserProfile, related_name='rating_user')
    userRated = models.ForeignKey(UserProfile, related_name='rated_user')
    rating = models.IntegerField()

    class Meta:
        unique_together = ('userRater', 'userRated')

#The requests that users make to join a trip.
class Requests(models.Model):
    user = models.ForeignKey(UserProfile)
    trip = models.ForeignKey(Trip)

    class Meta:
        unique_together = ('user', 'trip')

#The users that have been approved to join the trip + the creator of the trip.
class TripUsers(models.Model):
    user = models.ForeignKey(UserProfile)
    trip = models.ForeignKey(Trip)

    class Meta:
        unique_together = ('user', 'trip')

