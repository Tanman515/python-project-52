from django.shortcuts import render
from django.views.generic.list import ListView
from .models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task.utils.mixin import CustomLoginRequiredMixin, OwnerRequiredMixin
from django.utils.translation import gettext as _



class UsersList(ListView):
	model = User
	template_name = 'users/list.html'
	context_object_name = 'users'


class CreateUser(SuccessMessageMixin, CreateView):
	form_class = CreateUserForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')
	success_message = _('User successfully registered')


class DeleteView(CustomLoginRequiredMixin, OwnerRequiredMixin, DeleteView, SuccessMessageMixin):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _("User successfully deleted")


class UpdateView(CustomLoginRequiredMixin, OwnerRequiredMixin, SuccessMessageMixin, UpdateView):
	model = User
	form_class = UpdateUserForm
	template_name = 'users/update.html'
	success_url = reverse_lazy('users')
	success_message = _("User successfully changed")
