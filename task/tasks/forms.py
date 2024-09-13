from django import forms
from .models import Task
from django.utils.translation import gettext as _
from task.marks.models import Mark




class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        widgets = {
            'labels': forms.SelectMultiple,
        }