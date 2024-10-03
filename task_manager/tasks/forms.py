from django import forms
from .models import Task
from django.utils.translation import gettext as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {'name': _('Name'),
                  'description': _('Description'),
                  'status': _('Status'),
                  'executor': _('Executor'),
                  'labels': _('Labels')}
        widgets = {
            'label': forms.SelectMultiple,
        }
