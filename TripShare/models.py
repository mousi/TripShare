from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core import validators
import datetime
from datetime import date

def validate_greater_equal_zero(value):
    if value <= 0:
        raise ValidationError(u'%s is not greater or equal' % value)

def validate_greater_equal_one(value):
    if value <= 1:
	raise ValidationError(u'%s is not greater or equal' % value)


# Profile of Users. Users can have a driving licence, a car, number of ratings and averageRating.
# Used to add additional fields to the default Django User model.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes
    # Is this user a driver?
    isDriver = models.BooleanField(default=False)

    # Avatar (image)
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.jpg')

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

    #Ensure that save() cannot allow invalid values for cost and number of trip passengers
    def save(self, *args, **kwargs):
	if self.pass_num < 1:
		self.pass_num = 1
	if self.cost < 0:
		self.cost = 0
	
	current_date = datetime.datetime.today()

	if self.tripdate < current_date:
		self.tripdate = datetime.datetime.today()
	
        super(Trip, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.source + " to " + self.destination

# A user can rate another user with a rating.
class Rating(models.Model):
    userRater = models.ForeignKey(User, related_name='rating_user')
    userRated = models.ForeignKey(User, related_name='rated_user')
    rating = models.IntegerField()

    #Ensure that rating cannot be negative
    def save(self, *args, **kwargs):
	if self.rating < 0:
		self.rating = 0
        super(Rating, self).save(*args, **kwargs)


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
