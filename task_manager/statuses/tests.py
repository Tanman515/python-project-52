from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Status


class StatusTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(
            username='testuser', password='testpassword'
        )
        self.status = Status.objects.create(
            name='Test Status'
        )

    def test_create_status_get(self):
        url = reverse('create_status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/create.html')

    def test_create_status_post(self):
        url = reverse('create_status')
        status_data = {
            'name': 'New Status'
        }
        response = self.client.post(url, status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())

    def test_update_status_get(self):
        url = reverse('update_status', args=[self.status.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/update.html')

    def test_update_status_post(self):
        url = reverse('update_status', args=[self.status.pk])
        updated_data = {
            'name': 'Updated Status',
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses'))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')

    def test_delete_status_get(self):
        url = reverse('delete_status', args=[self.status.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/delete.html')

    def test_delete_status_post(self):
        url = reverse('delete_status', args=[self.status.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses'))
        self.assertFalse(Status.objects.filter(name='Test Status').exists())

    def test_status_list_get(self):
        url = reverse('statuses')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/list.html')
        self.assertContains(response, 'Test Status')
