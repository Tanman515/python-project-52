from django.db import models
from django.utils.translation import gettext as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.marks.models import Mark



class Task(models.Model):

	name = models.CharField(max_length=255, verbose_name=_('Name'))
	description = models.TextField(blank=True, null=True)
	status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, blank=False)
	author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_by', editable=False, null=False, blank=False)
	executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='task_for')
	label = models.ManyToManyField(Mark, related_name='task_label', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name