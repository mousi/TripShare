from django.shortcuts import render
from TripShare.models import Trip, TripUser, Request
from TripShare.forms import UserForm,UserProfileForm,TripForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):

    trips_list = Trip.objects.all()
    request_list = Request.objects.all()
    context_dict = {'trips':trips_list,'requests':request_list}

    return render(request, 'TripShare/index.html', context_dict)

def about(request):
    return render(request, 'TripShare/about.html', {})

def addTrip(request):

    if request.method == 'POST':
        form = TripForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return index(request)
        else:
            print form.errors
    else:

        form = TripForm()

    return render(request, 'TripShare/post.html', {'form' : form})



def test(request):
    context_dict = {}
    return render(request, 'TripShare/test.html', context_dict)

def user_login(request):
    print request.method

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        print username,password

        if user:

            if user.is_active:

                login(request,user)
                return HttpResponseRedirect('/TripShare/')
            else:

                return HttpResponse("Your account now is disabled.")
        else:

            return HttpResponseRedirect('/TripShare/')
    else:

        return render(request, 'TripShare/index.html', {})


def register(request):

    registered = False

    print request.method
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        if(user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'TripShare/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered' : registered})
	
def post(request):
    return render(request, 'TripShare/post.html', {})

def auth_logout(request):

    logout(request)
    return HttpResponseRedirect('TripShare/index.html')
