from django import forms
from .models import Mark
from django.utils.translation import gettext as _




class MarkForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=100)
    class Meta:
        model = Mark
        fields = ['name']