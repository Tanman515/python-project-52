from django.views.generic.list import ListView
from .models import Task
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from .forms import TaskForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin
from django.utils.translation import gettext as _



class TasksListView(CustomLoginRequiredMixin, ListView):
	model = Task
	template_name = 'tasks/list.html'
	context_object_name = 'tasks'


class CreateTaskView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
	form_class = TaskForm
	template_name = 'tasks/create.html'
	success_url = reverse_lazy('tasks')
	success_message = _("Task created successfully")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class DeleteTaskView(OwnerRequiredMixin, SuccessMessageMixin, CustomLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    permission_error_message = _('Only its author can delete a task')
    object_attr = 'author'


class UpdateTaskView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Task
	form_class = TaskForm
	template_name = 'tasks/update.html'
	success_url = reverse_lazy('tasks')
	success_message = _('Task successfully updated')

class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'