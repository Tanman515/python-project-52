from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Mark


class MarkTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.mark = Mark.objects.create(
            name='Test Label',
        )

    def test_create_mark_get(self):
        url = reverse('create_mark')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marks/create.html')

    def test_create_post(self):
        url = reverse('create_mark')
        mark_data = {
            'name': 'New Label'
        }
        response = self.client.post(url, mark_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('marks'))
        self.assertTrue(Mark.objects.filter(name='New Label').exists())

    def test_update_mark_get(self):
        url = reverse('update_mark', args=[self.mark.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marks/update.html')

    def test_update_mark_post(self):
        url = reverse('update_mark', args=[self.mark.pk])
        updated_data = {
            'name': 'Updated Label'
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('marks'))
        self.mark.refresh_from_db()
        self.assertEqual(self.mark.name, 'Updated Label')

    def test_delete_mark_view(self):
        url = reverse('delete_mark', args=[self.mark.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marks/delete.html')

    def test_delete_mark(self):
        url = reverse('delete_mark', args=[self.mark.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('marks'))
        self.assertFalse(Mark.objects.filter(name='Test Label').exists())

    def test_mark_list_view(self):
        url = reverse('marks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marks/list.html')
        self.assertContains(response, 'Test Label')
