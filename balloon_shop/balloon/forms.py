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
        fields = ['name',
                  'slug',
                  'description',
                  'price',
                  'photo',
                  'is_onsite',
                  'group']
        widgets = {'description': forms.Textarea(attrs={'cols': 60, 'rows': 15})}


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255, required=True)
    phone = forms.CharField(label='Телефон', required=True)
    information = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}),required=True)
    captcha = CaptchaField()


class LeaveReview(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True)
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}),
                                  required=True)
    photo = forms.ImageField(label='Фото', required=False)
    captcha = CaptchaField()


# class LeaveReview(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['Captcha'] = CaptchaField()
#
#     class Meta:
#         model = Review
#         fields = ['name',
#                   'text',
#                   'photo']





