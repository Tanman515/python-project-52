from django.views.generic.list import ListView
from .models import Mark
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import MarkForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin
from django.utils.translation import gettext as _



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


class UpdateMarkView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Mark
	form_class = MarkForm
	template_name = 'marks/update.html'
	success_url = reverse_lazy('marks')
	success_message = _('Mark successfully updated')
