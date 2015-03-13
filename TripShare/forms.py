from django import forms
from django.contrib.auth.models import User
from TripShare.models import User,UserProfile
from TripShare.models import Trip
from django.template.defaultfilters import slugify

class TripForm(forms.ModelForm):
    desc = forms.CharField(max_length=255,help_text="Please enter the description of your trip.")
    source = forms.CharField(max_length=30,help_text="Please enter the source of your trip.")
    destination = forms.CharField(max_length=30,help_text="Please enter the destination of your trip.")
    tripdate = forms.DateTimeField(help_text="Please enter the date you want to start the trip")
    cost = forms.FloatField(help_text="Enter the approximate cost of the trip")
    pass_num = forms.IntegerField(help_text="Enter the number of participants of trip")

    class Meta:
        model = Trip
        exclude = ('')



class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('isDriver','avatar')
