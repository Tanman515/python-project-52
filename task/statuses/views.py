from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Status
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .forms import CreateStatusForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin



class StatusesListView(ListView):
	model = Status
	template_name = 'statuses/list.html'
	context_object_name = 'statuses'


class CreateStatusView(SuccessMessageMixin, CreateView):
	form_class = CreateStatusForm
	template_name = 'statuses/create.html'
	success_url = reverse_lazy('statuses')
	success_message = "Статус успешно создан"


# class DeleteView(CustomLoginRequiredMixin, OwnerRequiredMixin, DeleteView):
#     model = User
#     template_name = 'users/delete.html'
#     success_url = reverse_lazy('users')


# class UpdateView(CustomLoginRequiredMixin, OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
# 	model = User
# 	form_class = UpdateUserForm
# 	template_name = 'users/update.html'
# 	success_url = reverse_lazy('users')
# 	success_message = "Пользователь успешно изменён"