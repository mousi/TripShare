from django.shortcuts import render
from TripShare.models import *
from TripShare.forms import *
from django.contrib.auth import *
from django.db.models import Avg, Count
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.decorators import login_required

import os
from django.core.context_processors import csrf

#Creates a request to join a trip.
@login_required
def join_trip(request):
    #Checks if the request is POST
    if request.method == 'POST':
        #Gets the user id and the trip id of the trip
        user_id = request.POST.get('user_id')
        trip_id = request.POST.get('trip_id')

        userakos = User.objects.get(id=user_id)
        tripaki = Trip.objects.get(id=trip_id)
        #If there is no request from that user to that trip, create a request
        Request.objects.get_or_create(user=userakos, trip=tripaki)
    return render(request, 'TripShare/index.html', {})

#User accepts or rejects a request.
@login_required
def respond_request(request):

    if request.method == 'GET':
        #Gets the choice: accept or decline.
        choice = request.GET['choice']
        request = request.GET['request']

        req = Request.objects.get(id=request)
        tripUsers = TripUser.objects.filter(trip=req.trip)

        totalPass = req.trip.pass_num
        acceptedPass = len(tripUsers)

        driverExists = False
        creatorProfile = UserProfile.objects.get(user=req.trip.creator)
        requesterProfile = UserProfile.objects.get(user=req.user)

        if creatorProfile.isDriver:
            driverExists = True
        elif requesterProfile.isDriver:
            driverExists = True
        else:
            for tUser in tripUsers:
                userProf = UserProfile.objects.get(user=tUser)
                if userProf.isDriver:
                    driverExists = True
                    break


        if choice == 'accept':
            # If there are more than one spots available in this trip
            if (totalPass - acceptedPass) > 1:
                req.reqAccepted = True
                TripUser.objects.get_or_create(user=req.user, trip=req.trip)
            # If there is only 1 spot available, we have to make sure that there is a driver in this trip
            elif (totalPass - acceptedPass) == 1:
                if driverExists:
                    req.reqAccepted = True
                    TripUser.objects.get_or_create(user=req.user, trip=req.trip)
                else:
                    return HttpResponse(False)
            else:
                return HttpResponse(False)
        else:
            req.reqAccepted = False
        #Saves the request to the database.
        req.save()
    return HttpResponse(True)

#View that handles the index page.
def index(request):
    context_dict = {}
    context_dict.update(csrf(request))

    #Shows only the trips that are going to be done in the future.
    current_date = datetime.datetime.now().date()
    trips_list = Trip.objects.filter(tripdate__gte = current_date).order_by('-dateposted').annotate(passengers=Count('tripuser'))

    #Get all the id of trips that user has requested to join
    request_list = Request.objects.filter(user = request.user.id).values_list('trip',flat = True)

    context_dict = {'trips': trips_list, 'requests': request_list}

    visits = request.session.get('visits')
    requested_trips = []

    context_dict['requested_trips'] = requested_trips
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

#About page.
def about(request):
    return render(request, 'TripShare/about.html', {})

#Add a trip to the database.
@login_required
def addTrip(request):

    if request.method == 'POST':
        #Gets the form's fields.
        form = TripForm(request.POST)

        #If the form's fields are valid.
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

#Handles user's login
def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authenticates the user.
        user = authenticate(username = username, password = password)

        if user:
            #If the user has not been deactivated by the admins.
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect('/TripShare/')
            else:
                return HttpResponse("Your account now is disabled.")
        else:
            return HttpResponseRedirect('/TripShare/')
    else:
        return render(request, 'TripShare/index.html', {})

#Handles user's register form.
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

@login_required
def post(request):
    return render(request, 'TripShare/post.html', {})

@login_required
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/TripShare/')

#View for viewing profiles.
@login_required
def view_profile(request, username):

    userviewed = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=userviewed)
    #User's date of birth.
    dob = profile.dob
    #Today
    today = datetime.datetime.today()

    #Calculates the age of the user.
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    #Gets the average rating of the user
    ratings = Rating.objects.filter(userRated=userviewed).aggregate(Avg('rating'))
    avgRating = ratings['rating__avg']

    try:
        myRating = Rating.objects.get(userRater=request.user,userRated=userviewed).rating
    except:
        myRating = 0

    try:
        #List of trips created by this user.
        created_list = Trip.objects.filter(creator=userviewed)
        #List of trips this user has been accepted to.
        joined_list = TripUser.objects.filter(user=userviewed)

    except Trip.DoesNotExist:
        created_list = None
        joined_trips = None

    context_dict={'age': age, 'created_list':created_list, 'joined_list':joined_list, 'user':request.user, 'user_viewed':userviewed, 'user_profile':profile, 'avgrating':avgRating, 'myrating':myRating}

    return render(request, 'TripShare/viewprofile.html', context_dict)


#Returns all the requests that have been submitted for a user's trips.
@login_required
def view_requests(request, username):
    user = User.objects.get(username=username)

    #Gets all the requests the user has submitted.
    user_requests = Request.objects.filter(user=user)

    #Gets all the trips that the user has created.
    user_trips = Trip.objects.filter(creator=user)
    #Gets the requests for the user's trips and annotate the number of passengers in each request's trip.
    other_requests = Request.objects.filter(trip=user_trips).annotate(passengers=Count('trip__tripuser'))

    context_dict = {'user_requests': user_requests, 'other_requests': other_requests}
    return render(request, 'TripShare/requests.html', context_dict)

#Gets a user's rating for another user. Recalculates the average rating of the user and stores it.
@login_required
def rate_user(request):
    # Checks if the request is POST
    if request.method == 'POST':
        # Gets the rated and rater user ids
        user_rated_id=request.POST.get('userrated_id')
        user_rater_id=request.POST.get('userrater_id')
        # Gets the rating
        rating = request.POST.get('rating')

        # Gets the two users by their ID
        rater = User.objects.get(id=user_rater_id)
        rated = User.objects.get(id=user_rated_id)

        # Stores the rating
        Rating.objects.update_or_create(userRater=rater, userRated=rated, defaults={'rating':rating})

        #Gets the average rating of the user
        ratings = Rating.objects.filter(userRated=rated).aggregate(Avg('rating'))
        avgRating = ratings['rating__avg']

    return HttpResponse(avgRating)
