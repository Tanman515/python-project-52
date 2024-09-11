from django import forms
from .models import Task
from django.utils.translation import gettext as _




class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']