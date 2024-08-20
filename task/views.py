from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'task/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Менеджер задач'
		return context
