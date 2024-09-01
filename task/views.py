from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(TemplateView):
	template_name = 'task/index.html'


class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'task/login.html'
    success_message = "Вы залогинены"

class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
