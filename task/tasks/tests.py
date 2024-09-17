from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task.tasks.models import Task
from task.statuses.models import Status
from task.marks.models import Mark


class TaskTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        self.status = Status.objects.create(
            name='Start',
        )
        self.label = Mark.objects.create(
            name='Big',
        )

        self.task = Task.objects.create(
            name='testtask',
            description='Text regarding current task',
            status=self.status,
            executor=self.user,
            author=self.user
        )
        self.task.label.add(self.label)

    def test_create_task_get(self):
        url = reverse('create_task')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/create.html')

    def test_create_task_post(self):
        url = reverse('create_task')
        task_data = {
            'name': 'New Task',
            'description': 'New Description',
            'status': self.status.id,
            'executor': self.user.id,
            'label': [self.label.id]
        }
        response = self.client.post(url, task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))
        self.assertTrue(Task.objects.filter(name='New Task').exists())

    def test_update_task_get(self):
        url = reverse('update_task', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/update.html')

    def test_update_task_post(self):
        url = reverse('update_task', args=[self.task.pk])
        updated_data = {
            'name': 'Updated Task',
            'description': 'Updated Description',
            'status': self.status.id,
            'executor': self.user.id,
            'label': [self.label.id]
        }
        response = self.client.post(url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Updated Task')
        self.assertEqual(self.task.description, 'Updated Description')

    def test_delete_task_get(self):
        url = reverse('delete_task', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/delete.html')

    def test_delete_task(self):
        url = reverse('delete_task', args=[self.task.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))
        self.assertFalse(Task.objects.filter(name='testtask').exists())

    def test_task_list_get(self):
        url = reverse('tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/list.html')
        self.assertContains(response, 'testtask')

    def test_task_detail_view(self):
        url = reverse('task_view', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/detail.html')
        self.assertContains(response, 'testtask')
