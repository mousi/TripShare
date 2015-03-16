from django import forms
from TripShare.models import User,UserProfile
from TripShare.models import Trip
from django.contrib.auth.forms import UserCreationForm

class TripForm(forms.ModelForm):
    desc = forms.CharField(max_length=255,help_text="Please enter the description of your trip.")
    source = forms.CharField(max_length=30,help_text="Please enter the source of your trip.")
    destination = forms.CharField(max_length=30,help_text="Please enter the destination of your trip.")
    tripdate = forms.DateTimeField(help_text="Please enter the date you want to start the trip")
    cost = forms.FloatField(help_text="Enter the approximate cost of the trip")
    pass_num = forms.IntegerField(help_text="Enter the number of participants of trip")
    #dateposted = forms.DateTimeField(help_text = "Date trip posted", widget = forms.HiddenInput(), required = False)
    class Meta:
        model = Trip
        exclude = ('creator','dateposted',)

class UserForm(UserCreationForm):

    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    #password = forms.CharField(widget = forms.PasswordInput,label="Password")
    #password2 = forms.CharField(widget = forms.PasswordInput,label="Password (again)")

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob','isDriver','avatar')
