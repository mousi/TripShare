from django.shortcuts import render
from TripShare.models import Trip, TripUser, Request, User, UserProfile
from TripShare.forms import UserForm,UserProfileForm,TripForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
import datetime

import os

def index(request):
    trips_list = Trip.objects.all()
    request_list = Request.objects.all()
    context_dict = {'trips':trips_list, 'requests':request_list}
    visits = request.session.get('visits')

    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.datetime.now())
        request.session['visits'] = visits

    context_dict['visits'] = visits
    visits = request.session.get('visits')

    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits

    return render(request, 'TripShare/index.html', context_dict)

def about(request):
    return render(request, 'TripShare/about.html', {})

def addTrip(request):

    if request.method == 'POST':

        form = TripForm(request.POST)

        if form.is_valid():

            trip = form.save(commit = False)

            trip.creator = request.user

            trip.save()

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

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {}
    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered']= registered

    return render(request, 'TripShare/register.html', context_dict)

def post(request):
    return render(request, 'TripShare/post.html', {})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/TripShare/')


def view_profile(request, username):

    user = User.objects.get(username=username)
    try:
        joined_trips = []

        created_list = Trip.objects.filter(creator=user)

        #Returns a list of dictionaries
        joined_list = TripUser.objects.filter(user=user)

        for d in joined_list:
            joined_trips.append(d.trip)


    except Trip.DoesNotExist:
        created_list = None
        joined_list = None

    context_dict={'created_list':created_list, 'joined_list':joined_list}

    return render(request, 'TripShare/viewprofile.html', context_dict)

