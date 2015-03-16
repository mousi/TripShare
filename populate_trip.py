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
                                 avatar="avatars/rango.jpg",
                                 dob=datetime.date(1984,5,21))

    user_liverpoolaras = add_userProfile(username="liverpoolaras",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             isDriver=True,
             avatar="avatars/gavros.jpg",
             email="dummy_email2@tripshare.co.uk",
             first_name="Vag",
             last_name="Karv",
             dob=datetime.date(1999,5,19))
    user_geo = add_userProfile(username="geo",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             first_name="Geo",
             last_name="Gv",
             dob=datetime.date(1994,5,4))
    user_thanos = add_userProfile(username="thanos",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             first_name="Thanos",
             last_name="S",
             email="dummy_email3@tripshare.co.uk",
             dob=datetime.date(1994,3,4))
    user_jenny = add_userProfile(username="jenny",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             isDriver=True,
             dob=datetime.date(1998,12,1))
    user_molester = add_userProfile(username="molester",
             password="pbkdf2_sha256$15000$zenpFl9q2m5Y$j86TIRkMKfMfaFuO11YY2An9cD4jUofWInw8QCJk83I=",
             dob=datetime.date(1966,2,9))

    # Add some trips
    trip1=add_trip(description="A road trip from Glasgow to London. We will stop in Liverpool to see THE TEAM!",
             creator=user_mousi,
             source="Glasgow",
             destination="London",
             pass_num=3,
             cost=30,
             tripdate=datetime.datetime(2015,4,5,10,0,0),
             dateposted = datetime.datetime(2015,4,2,10,0,0))
    trip2=add_trip(description="Looking for someone with a car to travel to Manchester from Aberdeen",
             creator=user_liverpoolaras,
             source="Aberdeen",
             destination="manchester",
             pass_num=1,
             tripdate=datetime.datetime(2015,4,11,9,0,0),
             dateposted = datetime.datetime(2015,4,10,8,0,0),
             cost=10)
    trip3=add_trip(description="Going from Birmingham to Newcastle",
                   creator=user_geo,
                   source="Birmingham",
                   destination="Newcastle",
                   pass_num=10,
                   tripdate=datetime.datetime(2015,5,1,12,0,0),
                   dateposted = datetime.datetime(2015,4,2,12,0,0))

    trip4=add_trip(description="Going from Glasgow to Dundee",
                   creator=user_jenny,
                   source="Glasgow",
                   destination="Dundee",
                   pass_num=5,
                   cost=30,
                   tripdate=datetime.datetime(2015,5,13,13,30,0),
                   dateposted = datetime.datetime(2015,4,2,12,0,0)
    
    trip5=add_trip(description="Going from Dundee to Glasgow",
                   creator=user_geo,
                   source="Dundee",
                   destination="Glasgow",
                   pass_num=4,
                   cost=15,
                   tripdate=datetime.datetime(2015,6,15,7,30,0),
                   dateposted = datetime.datetime(2015,5,5,10,0,0)

    trip6=add_trip(description="Going from Manchester to Glasgow",
                   creator=user_mousi,
                   source="Manchester",
                   destination="Glasgow",
                   pass_num=12,
                   cost=18,
                   tripdate=datetime.datetime(2015,6,15,9,30,0),
                   dateposted = datetime.datetime(2015,2,2,8,0,0)

    trip7=add_trip(description="Going from Southampton to Glasgow",
                   creator=user_liverpoolas,
                   source="Southampton",
                   destination="Glasgow",
                   pass_num=2,
                   cost=23,
                   tripdate=datetime.datetime(2015,9,25,14,30,0),
                   dateposted = datetime.datetime(2015,7,1,10,0,0)

    )
    # Add some requests
    add_request(user=user_thanos, trip=trip1)
    add_request(user=user_geo, trip=trip1)
    add_request(user=user_jenny, trip=trip1, reqAccepted=True)
    add_request(user=user_molester, trip=trip2, reqAccepted=True)

    # Add the accepted users to the trips
    add_user_trip(user=user_molester, trip=trip2)
    add_user_trip(user=user_jenny, trip=trip1)

    # Add some ratings
    add_rating(user_jenny, user_molester, 5)
    add_rating(user_thanos, user_liverpoolaras, 1)


def add_trip(description, creator, source, destination, pass_num, tripdate, dateposted, cost=None):
    trip=Trip.objects.get_or_create(desc=description, creator=creator, source=source, destination=destination, pass_num=pass_num, cost=cost, tripdate=tripdate, dateposted = dateposted)[0]
    return trip

def add_request(user, trip, reqAccepted=None):
    req=Request.objects.get_or_create(user=user, trip=trip, reqAccepted=reqAccepted)[0]
    return req

def add_user_trip(user, trip):
    ut=TripUser.objects.get_or_create(user=user,trip=trip)[0]
    return ut

def add_rating(userRater, userRated, rating):
    r=Rating.objects.get_or_create(userRater=userRater, userRated=userRated, rating=rating)[0]
    return r

def add_userProfile(username, password, dob, isDriver=False, avatar="avatars/default.jpg", email="", first_name="",last_name=""):
    user = add_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    up = UserProfile.objects.get_or_create(user=user, isDriver=isDriver, avatar=avatar, dob=dob)[0]
    return user

def add_user(username, password, email, first_name, last_name):
    u = User.objects.get_or_create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)[0]
    return u

# Start execution here!
if __name__ == '__main__':
    print "Starting TripShare population script..."
    populate()
