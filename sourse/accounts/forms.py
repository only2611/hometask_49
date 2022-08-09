from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(forms.ModelForm):

    # class Meta(UserCreationForm.Meta):
    #     email = forms.EmailField(label="Почта", required=False, )
    #     fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name = cleaned_data.get('first_name')
    #     if not first_name:
    #         raise ValueError('Заполните хотя бы это поле')

    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label="Почта", required=True,)
    # last_name = forms.CharField(label="Last_name", required=True,)
    # first_name = forms.CharField(label="First_name", required=True, )

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']



    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return  user



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        if password != password_confirm:
            raise ValidationError('Пароли не совпадают')
        if not last_name and not first_name:
            raise ValidationError("Надо заполнить хоть одно поле: Last name или First name")
        else:
            return cleaned_data






