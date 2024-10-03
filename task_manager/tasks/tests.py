from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.marks.models import Mark


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
        self.labels = Mark.objects.create(
            name='Big',
        )

        self.task = Task.objects.create(
            name='testtask',
            description='Text regarding current task',
            status=self.status,
            executor=self.user,
            author=self.user
        )
        self.task.labels.add(self.labels)

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
            's': [self.labels.id]
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
            'labels': [self.labels.id]
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


class TaskFilterTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username='testuser1',
            password='password'
        )
        self.user2 = get_user_model().objects.create_user(
            username='testuser2',
            password='password'
        )
        self.client.login(username='testuser1', password='password')

        self.status1 = Status.objects.create(
            name='In development',
        )
        self.status2 = Status.objects.create(
            name='Finished',
        )

        self.label1 = Mark.objects.create(
            name='Bug'
        )
        self.label2 = Mark.objects.create(
            name='Feature'
        )

        self.task1 = Task.objects.create(
            name='Task 1',
            description='Description 1',
            status=self.status1,
            executor=self.user1,
            author=self.user1
        )
        self.task1.labels.add(self.label1)

        self.task2 = Task.objects.create(
            name='Task 2',
            description='Description 2',
            status=self.status2,
            executor=self.user2,
            author=self.user2
        )
        self.task2.labels.add(self.label2)

    def test_filter_by_status(self):
        url = reverse('tasks')
        response = self.client.get(url, {'status': self.status1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_filter_by_executor(self):
        url = reverse('tasks')
        response = self.client.get(url, {'executor': self.user1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_filter_by_labels(self):
        url = reverse('tasks')
        response = self.client.get(url, {'labels': self.label1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_filter_self_tasks(self):
        url = reverse('tasks')
        response = self.client.get(url, {'self_tasks': 'on'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')

    def test_filter_combined(self):
        url = reverse('tasks')
        response = self.client.get(url, {
            'status': self.status1.id,
            'executor': self.user1.id,
            'labels': self.label1.id,
            'self_tasks': 'on'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')
