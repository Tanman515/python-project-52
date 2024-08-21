from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class IndexView(TemplateView):
	template_name = 'task/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = _('Task manager')
		return context
