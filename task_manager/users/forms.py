from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext as _


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        label=_('User name'),
        max_length=150,
        help_text = _('Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.') # noqa
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
        help_text=_('Your password must contain at least 3 characters.')
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(),
        help_text=_('To confirm, please enter your password again.')
    )
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(),
        max_length=150,
        help_text = _('Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.') # noqa
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
        help_text=_('Your password must contain at least 3 characters.'),
        error_messages={'required': ''}
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(),
        help_text=_('To confirm, please enter your password again.'),
        error_messages={'required': ''}
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('The passwords do not match.'))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
