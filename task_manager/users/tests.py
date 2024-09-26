from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='Testpassword',
            first_name='Test',
            last_name='User'
        )
        self.client.login(username='testuser', password='Testpassword')

    def test_update_user_get(self):
        url = reverse('update', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

    def test_update_user_post(self):
        url = reverse('update', args=[self.user.pk])
        updated_data = {
            'username': 'updateduser',
            'password1': 'Newpassword',
            'password2': 'Newpassword',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.first_name, 'Updated')
        self.assertEqual(self.user.last_name, 'User')

    def test_delete_user_get(self):
        url = reverse('delete', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

    def test_delete_user_post(self):
        url = reverse('delete', args=[self.user.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users'))
        self.assertFalse(get_user_model().objects.filter(
            username='testuser'
        ).exists())

    def test_user_list_view(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/list.html')
        self.assertContains(response, 'testuser')


class CreateUserTest(TestCase):
    def test_create_user_get(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_create_user(self):
        url = reverse('register')
        user_data = {
            'username': 'testuser',
            'password1': 'Testpassword',
            'password2': 'Testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(get_user_model().objects.filter(
            username='testuser'
        ).exists())
