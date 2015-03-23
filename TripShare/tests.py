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
	   Checks if model Rating accepts rating < 0
	"""

	"""def test_ensure_rating_is_not_negative(self):


		user = User.objects.get_or_create(id=10)[0]
		user1 = User.objects.get_or_create(id=9)[0]

		
		rating_test = Rating(user,user,-1)
		rating_test.save()
		self.assertEqual((rating_test.rating >= 0), True)"""

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

	def test_index_view_with_registers(self):
    		"""
   		 Register a user and check if is in DB.
   		 """
		c = Client()
		response = c.post('/login/', {'username': 'geo', 'password': 'tripshare'})
		response.status_code
		response = c.get('/viewprofile/')
		response.content


