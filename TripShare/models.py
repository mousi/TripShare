from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes
    driver = models.BooleanField(default=False)
    hasCar = models.BooleanField(default=False)
    numRatings = models.IntegerField(default=0)
    avgRating = models.FloatField(null=True)

    def __unicode__(self):
        return self.user.username

class Trip(models.Model):
    desc = models.CharField(max_length=255)
    creator = models.ForeignKey(UserProfile)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    pass_num = models.IntegerField(default=0)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.desc

class Ratings(models.Model):
    userRater = models.ForeignKey(UserProfile, related_name='rating_user')
    userRated = models.ForeignKey(UserProfile, related_name='rated_user')
    rating = models.IntegerField(default=0)

    class Meta:
        unique_together = ('userRater', 'userRated')

class Requests(models.Model):
    user = models.ForeignKey(UserProfile)
    trip = models.ForeignKey(Trip)

    class Meta:
        unique_together = ('user', 'trip')

class TripUsers(models.Model):
    user = models.ForeignKey(UserProfile)
    trip = models.ForeignKey(Trip)
    driver = models.BooleanField(default=False)
    usersCar = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'trip')

