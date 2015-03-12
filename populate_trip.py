import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TripShareProject.settings')

import django
django.setup()

import datetime

from TripShare.models import User, UserProfile, Trip, Rating, Request, TripUser


def populate():
    # Add some users
    user_mousi = add_userProfile(username="mousi",
                                 password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
                                 isDriver=True,
                                 first_name="Kostas",
                                 last_name="K",
                                 email="dummy_email@tripshare.co.uk",
                                 avatar="avatars/rango.jpg")

    user_liverpoolaras = add_userProfile(username="liverpoolaras",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             isDriver=True,
             avatar="avatars/gavros.jpg",
             email="dummy_email2@tripshare.co.uk",
             first_name="Vag",
             last_name="Karv")
    user_geo = add_userProfile(username="geo",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             first_name="Geo",
             last_name="Gv")
    user_thanos = add_userProfile(username="thanos",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             first_name="Thanos",
             last_name="S",
             email="dummy_email3@tripshare.co.uk")
    user_jenny = add_userProfile(username="jenny",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             isDriver=True)
    user_molester = add_userProfile(username="molester",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=")

    # Add some trips
    trip1=add_trip(description="A road trip from Glasgow to London. We will stop in Liverpool to see THE TEAM!",
             creator=user_mousi,
             source="Glasgow",
             destination="London",
             pass_num=3,
             tripdate=datetime.datetime(2015,4,1,10,0,0),
             dateposted = datetime.datetime(2015,4,2,10,0,0),
             carOwner=user_mousi)
    trip2=add_trip(description="Looking for someone with a car to travel to Manchester from Aberdeen",
             creator=user_liverpoolaras,
             source="Aberdeen",
             destination="manchester",
             pass_num=1,
             tripdate=datetime.datetime(2015,4,11,9,0,0),
             dateposted = datetime.datetime(2015,4,10,8,0,0),
             carOwner=user_molester)
    trip3=add_trip(description="Going from Birmingham to Newcastle",
                   creator=user_geo,
                   source="Birmingham",
                   destination="Newcastle",
                   tripdate=datetime.datetime(2015,5,1,12,0,0),
                   dateposted = datetime.datetime(2015,4,2,12,0,0))

    trip4=add_trip(description="Going from Glasgow to Dundee",
                   creator=user_jenny,
                   source="Glasgow",
                   destination="Dundee",
                   pass_num=5,
                   cost=30,
                   datetime=datetime.datetime(2015,5,13,13,30,0)
                   )

    # Add some requests
    add_request(user=user_thanos, trip=trip1)
    add_request(user=user_geo, trip=trip1)
    add_request(user=user_jenny, trip=trip1, reqAccepted=True)
    add_request(user=user_molester, trip=trip2, hasCar=True, passengers=1, cost=50.99, reqAccepted=True)

    # Add the accepted users to the trips
    add_user_trip(user=user_molester, trip=trip2)
    add_user_trip(user=user_jenny, trip=trip1)

    # Add some ratings
    add_rating(user_jenny, user_molester, 5, "Very good guy. Had loads of fun in our last trip! ;)")
    add_rating(user_thanos, user_liverpoolaras, 1, "Really boring guy... Was sleeping during the entire trip!")


def add_trip(description, creator, source, destination, tripdate, dateposted, carOwner=None, pass_num=None, cost=None):
    trip=Trip.objects.get_or_create(desc=description, creator=creator, source=source, destination=destination, pass_num=pass_num, cost=cost, tripdate=tripdate, dateposted = dateposted, carOwner=carOwner)[0]
    return trip

def add_request(user, trip, hasCar=False, passengers=None, cost=None, reqAccepted=None):
    req=Request.objects.get_or_create(user=user, trip=trip, hasCar=hasCar, passengers=passengers, cost=cost, reqAccepted=reqAccepted)[0]
    return req

def add_user_trip(user, trip):
    ut=TripUser.objects.get_or_create(user=user,trip=trip)[0]
    return ut

def add_rating(userRater, userRated, rating, comments=""):
    r=Rating.objects.get_or_create(userRater=userRater, userRated=userRated, rating=rating, comments=comments)[0]
    return r

def add_userProfile(username, password, isDriver=False, avatar="", email="", first_name="",last_name=""):
    user = add_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    up = UserProfile.objects.get_or_create(user=user, isDriver=isDriver, avatar=avatar)[0]
    return up

def add_user(username, password, email, first_name, last_name):
    u = User.objects.get_or_create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)[0]
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting TripShare population script..."
    populate()
