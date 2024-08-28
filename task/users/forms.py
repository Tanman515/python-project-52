from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms



class CreateUserForm(UserCreationForm):
	username = forms.CharField(
		label='Имя пользователя',
		max_length=150,
		help_text = 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'
	)
	password1 = forms.CharField(
		label='Пароль',
		widget=forms.PasswordInput(),
		help_text='Ваш пароль должен содержать как минимум 3 символа.'
	)
	password2 = forms.CharField(
		label='Подтверждение пароля',
		widget=forms.PasswordInput(),
		help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.')
	usable_password = None

	class Meta:
		model = get_user_model()
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UpdateUserForm(UserChangeForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(),
        max_length=150,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(),
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        error_messages={'required': ''}
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
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
            self.add_error('password2', 'Пароли не совпадают.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user