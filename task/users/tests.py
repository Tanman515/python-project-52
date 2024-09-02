from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import User


class TestCRUD(TestCase):

	def setUp(self):
		self.client = Client()
		User.objects.create_user('Oleg', 'asdf@mail.ru', '123')


	def test_create_GET(self):
		response = self.client.get(reverse('register'))
		
		self.assertEqual(response.status_code, 200)


	def test_update_GET(self):
		response = self.client.get(reverse('update', args=[1, ]))
		
		self.assertEqual(response.status_code, 200)


	def test_delete_GET(self):
		response = self.client.get(reverse('delete', args=[1, ]))
		
		self.assertEqual(response.status_code, 200)
		
	
	def test_create_POST(self):
		self.client.post(reverse('register'), {'first_name': 'Kirill',
														  'last_name': 'Ivanov',
														  'username': 'Kirril',
														  'password1': '123',
														  'password2': '123'})
		
		self.assertEqual(len(User.objects.all()), 2)
		
	
	def test_delete_POST(self):
		self.client.post(reverse('delete', args=[1, ]))
		
		self.assertEqual(len(User.objects.all()), 0)
		
	def test_update_POST(self):
		self.client.post(reverse('update', args=[1, ]), {'first_name': 'New',
														  'last_name': 'User',
														  'username': 'Gena',
														  'password1': '123',
														  'password2': '123'})
		self.assertEqual(User.objects.filter(pk=1).values()[0]['username'], 'Gena')
