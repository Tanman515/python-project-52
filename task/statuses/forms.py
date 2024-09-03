from django import forms
from .models import Status



class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(label='Имя', max_length=100)
    class Meta:
        model = Status
        fields = ['name',]