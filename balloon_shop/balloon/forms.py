from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import *


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Выберите группу товара'

    class Meta:
        model = Balloon
        fields = ['name', 'slug', 'description', 'price', 'photo', 'is_onsite', 'group']


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    captcha = CaptchaField(label='Решите пример:')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    captcha = CaptchaField(label='Решите пример:')


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, required=True)
    phone = forms.CharField(label='Телефон', required=True)
    information = forms.CharField(label='Сообщение',
                                  widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}),
                                  required=True)
    captcha = CaptchaField(label='Решите пример:')


class LeaveReview(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), required=True)
    photo = forms.ImageField(label='Фото', required=False)
    captcha = CaptchaField(label='Решите пример:')






