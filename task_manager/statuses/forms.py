from django import forms
from .models import Status
from django.utils.translation import gettext as _


class StatusForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=100)

    class Meta:
        model = Status
        fields = ['name']
