from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			messages.error(request, 'Вы не залогинены! Пожалуйста, залогиньтесь.')
			return redirect('login')
		return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin:
	def dispatch(self, request, *args, **kwargs):
		user = self.request.user
		if user.id == int(kwargs.get('pk')):
			return super().dispatch(request, *args, **kwargs)
		messages.error(request, 'У вас нет прав для изменения другого пользователя.')
		return redirect('users')
