from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Status
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .forms import StatusForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin
from django.utils.translation import gettext as _



class StatusesListView(CustomLoginRequiredMixin ,ListView):
	model = Status
	template_name = 'statuses/list.html'
	context_object_name = 'statuses'


class CreateStatusView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
	form_class = StatusForm
	template_name = 'statuses/create.html'
	success_url = reverse_lazy('statuses')
	success_message = _("Status created successfully")


class DeleteStatusView(SuccessMessageMixin, CustomLoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')


class UpdateStatusView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Status
	form_class = StatusForm
	template_name = 'statuses/update.html'
	success_url = reverse_lazy('statuses')
	success_message = _('Status successfully updated')