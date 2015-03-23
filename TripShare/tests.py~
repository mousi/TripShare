from django.test import TestCase
from TripShare.models import Trip,UserProfile,Rating
from django.contrib.auth.models import User
import datetime
import time
from django.core.urlresolvers import reverse
from django.test.client import Client

class TripMethodTests(TestCase):
	"""
	   Checks if model Trip accepts number of passengers < 1
	"""
	def test_ensure_pass_num_is_less_than_1(self):
		user2 = User(id = 1)

		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate=datetime.datetime(2015,5,1,12,0,0),dateposted='2015-02-03')
		trip.save()
		self.assertEqual((trip.pass_num >= 1), True)
	"""
	   Checks if model Trip accepts cost < 0
	"""

	def test_ensure_cost_is_positive(self):
		user2 = User(id = 1)
		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate=datetime.datetime(2015,5,1,12,0,0),dateposted='2015-02-03')
		trip.save()
		self.assertEqual((trip.cost >= 0), True)

	"""
	   Check if model Trip accepts tripdate < current date
	"""

	def test_ensure_tripdate_is_not_pas(self):

		user2 = User(id = 1)
		



		trip = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate =datetime.datetime(2013,5,1,12,0,0),dateposted='2015-02-03')
		today = datetime.datetime.today()
		trip.save()

		
		self.assertEqual((trip.tripdate >= today), True)

	
	"""
	    If no trips exist, an appropriate message sould be displayed
	"""

	def test_index_view_with_no_trips(self):
        	
        	response = self.client.get(reverse('index'))
        	self.assertEqual(response.status_code, 200)


	"""
   		Populate a new trip to the back-end and then check the response.
   	"""
	def test_index_view_with_trips(self):
    		
		user2 = User(id = 1)

		t = Trip(desc='test',creator = user2,source='tests',destination='testd',pass_num=-1,cost=-1,tripdate =datetime.datetime(2013,5,1,12,0,0),dateposted='2015-02-03')
		
		t.save()




    		response = self.client.get(reverse('index'))
    		self.assertEqual(response.status_code, 200)
    		self.assertContains(response, 'test')

	def test_login_view_for_an_existing_user(self):
    		"""
   		 Tries to login an existing user.
		 Then checks viewprofile view.
   		 """
		c = Client()
		response = c.post('/user_login/', {'username': 'geo', 'password': 'tripshare'})
		response.status_code
		response = c.get('/viewprofile/')
		response.content

	"""
		Tests view rate_user.
		Then checks viewprofile view.
	"""
	
	def test_view_rate_user(self):

		c = Client()
		response = c.post('/rate_user/',{'userratedid': '1', 'userraterid': '2', 'rating': '3'})
		response.status_code
		response = c.get('/viewprofile/')
	


	"""
		Tests view join_trip
		Then checks viewprofile view.
	"""

	def test_view_join_trip(self):
		
		c = Client()
		response = c.post('/join_trip/',{'userid': '1', 'tripid': '2'})
		response.status_code
		response = c.get('/viewprofile/')

	"""
		Tests view add_trip
		Adds a new trip and then checks index view
	"""
	def test_view_add_trip(self):
		
		c = Client()
		response = c.post('/add_trip/',{'desc': 'Senegal', 'creator': 'user_mousi', 'source':'Senegal', 'destination':'Nigeria', 'pass_num': '2', 'cost': '1', 'tripdate': '2015-04-04', 'dateposted': '2015-03-03'})
		response.status_code
		reponse = c.get('/index/')

	

