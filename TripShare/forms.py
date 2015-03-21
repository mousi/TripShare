from django import forms
from TripShare.models import User,UserProfile
from TripShare.models import Trip
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget

class TripForm(forms.ModelForm):
    desc = forms.CharField(label="Description",max_length=255,widget=forms.Textarea)
    source = forms.CharField(label="From",max_length=30)
    destination = forms.CharField(label="To",max_length=30)
    tripdate = forms.DateTimeField(label="Date Time",input_formats=['%d.%m.%Y %H:%M'])
    cost = forms.FloatField(label="Cost",min_value=0,initial=0)
    pass_num = forms.IntegerField(label="Passengers",min_value=0,initial=1)

    class Meta:
        model = Trip
        fields = ('source','destination','tripdate','pass_num','cost','desc')

class UserForm(UserCreationForm):

    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('dob','isDriver','avatar')

class EditUserForm(UserCreationForm):
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        exclude = ('username',)
        exclude = ['first_name']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob','isDriver','avatar')
        exclude = ['dob','username']

