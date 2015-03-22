from django import forms
from TripShare.models import User,UserProfile
from TripShare.models import Trip
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget

#Form for posting trips
class TripForm(forms.ModelForm):
    #Description of the trip.
    desc = forms.CharField(label="Description",max_length=255,widget=forms.Textarea)
    source = forms.CharField(label="From",max_length=30)
    destination = forms.CharField(label="To",max_length=30)
    #Trip date.
    tripdate = forms.DateTimeField(label="Date Time",input_formats=['%d.%m.%Y %H:%M'])
    #Trip cost
    cost = forms.FloatField(label="Cost",min_value=0,initial=0)
    #Number of passenger
    pass_num = forms.IntegerField(label="Passengers",min_value=0,initial=1)

    #Fields to be included in the form.
    class Meta:
        model = Trip
        fields = ('source','destination','tripdate','pass_num','cost','desc')

#Used during registration to register a user.
class UserForm(UserCreationForm):

    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

#Used during registration to register a user's custom fields.
class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(label="Date of birth")
    isDriver = forms.BooleanField(label="Are you a driver?")
    class Meta:
        model = UserProfile
        fields = ('dob','isDriver','avatar')