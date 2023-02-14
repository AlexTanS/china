from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms

from .models import user_registrated, AdvUser


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=100, label="Логин")
    email = forms.EmailField(required=True, label="Электронная почта")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html(), validators=[
            RegexValidator(regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                           message="Пароль должен содержать не менее 8 латинских символов и не менее 1 цифры")])

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_active = False  # является ли пользователь активным
        user.is_activated = False  # прошел ли подтверждение регистрации
        if commit:
            user.save()
        user_registrated.send(RegisterUserForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ['username', "first_name", "last_name", 'email', 'password', "send_messages"]
