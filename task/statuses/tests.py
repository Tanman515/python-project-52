from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Status
from task.users.models import User


class TestCRUD(TestCase):

	def setUp(self):
		self.client = Client()
		current_status = {'name': 'first_status'}
		user_data = {'username': 'testuser',
					 'password': 'secret'}
		User.objects.create_user(**user_data)
		self.client.post(reverse('login'), user_data)
		Status.objects.create(**current_status)



	def test_create_status_GET(self):
		response = self.client.get(reverse('create_status'))
		
		self.assertEqual(response.status_code, 200)


	def test_update_GET(self):
		response = self.client.get(reverse('update_status', args=[1, ]))
		
		self.assertEqual(response.status_code, 200)


	def test_delete_GET(self):
		response = self.client.get(reverse('delete_status', args=[1, ]))
		
		self.assertEqual(response.status_code, 200)
		
	
	def test_create_POST(self):
		self.client.post(reverse('create_status'), {'name': 'second_status'})
		
		self.assertEqual(len(Status.objects.all()), 2)
		
	
	def test_delete_POST(self):
		self.client.post(reverse('delete_status', args=[1, ]))
		
		self.assertEqual(len(Status.objects.all()), 0)
		
	def test_update_POST(self):
		self.client.post(reverse('update_status', args=[1, ]), {'name': 'changed_status'})
		self.assertEqual(Status.objects.filter(pk=1).values()[0]['name'], 'changed_status')
