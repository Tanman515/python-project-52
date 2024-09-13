from django.db import models
from django.utils.translation import gettext as _



class Task(models.Model):
	class Meta:
		unique_together = ('author', 'executor')

	name = models.CharField(max_length=255, verbose_name=_('Name'))
	description = models.TextField()
	status = models.ForeignKey('statuses.Status', on_delete=models.PROTECT)
	author = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='created_by', editable=False)
	executor = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True, related_name='task_for')
	label = models.ForeignKey('marks.Mark', on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name