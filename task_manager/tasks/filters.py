import django_filters
from .models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.marks.models import Mark
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=Status.objects.order_by('id'),
        widget=forms.Select(attrs={'class': 'form-select mr-3 ml-2'})
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        queryset=User.objects.order_by('id'),
        widget=forms.Select(attrs={'class': 'form-select mr-3 ml-2'})
    )
    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=Mark.objects.order_by('id'),
        widget=forms.Select(attrs={'class': 'form-select mr-3 ml-2'})
    )
    self_tasks = django_filters.BooleanFilter(
        label=_('Only your tasks'),
        method='owner_tasks_filter',
        widget=forms.CheckboxInput(attrs={'class': 'mr-3'}),
        required=False
    )

    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'executor': ['exact'],
            'labels': ['exact'],
        }

    def owner_tasks_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
