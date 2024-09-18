from django.views.generic.list import ListView
from .models import Mark
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import MarkForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect



class MarksListView(CustomLoginRequiredMixin, ListView):
	model = Mark
	template_name = 'marks/list.html'
	context_object_name = 'marks'


class CreateMarkView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
	form_class = MarkForm
	template_name = 'marks/create.html'
	success_url = reverse_lazy('marks')
	success_message = _("Mark created successfully")


class DeleteMarkView(SuccessMessageMixin, CustomLoginRequiredMixin, DeleteView):
    model = Mark
    template_name = 'marks/delete.html'
    success_url = reverse_lazy('marks')
    success_message = _('Mark successfully deleted')

    def post(self, request, *args, **kwargs):
    	self.object = self.get_object()
    	if self.object.task_label.all().exists():
    		messages.error(request, _('Cannot remove label because it is in use'))
    		return redirect(self.success_url)
    	return super().post(request, *args, **kwargs)


class UpdateMarkView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Mark
	form_class = MarkForm
	template_name = 'marks/update.html'
	success_url = reverse_lazy('marks')
	success_message = _('Mark successfully updated')
