from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import *

menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Наши работы", "url_name": "works"},
    {"title": "Доставка", "url_name": "delivery"},
    {"title": "Отзывы", "url_name": "reviews"},
]


class HomePage(DataMixin, ListView):
    model = Balloon
    template_name = 'balloon/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Главная страница')
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context

    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True)


class ShowGoodsInGroup(DataMixin, ListView):
    model = Balloon
    template_name = "balloon/index.html"
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=str(context['goods'][0].group),
                                              group_selected=context['goods'][0].group_id)
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context

    def get_queryset(self):
        return Balloon.objects.filter(group__slug=self.kwargs['group_slug'], is_onsite=True)


class CertainProduct(DataMixin, DetailView):
    model = Balloon
    template_name = 'balloon/show_product.html'
    slug_url_kwarg = 'good_slug'
    context_object_name = 'good'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=context['good'])
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context


class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'balloon/add_product.html'
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Добавление товара на сайт')
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не существует!!!<h1>")


def about(request):
    groups = Group.objects.all()
    context = {
        'title': 'О нас',
        'menu': menu,
        'groups': groups,
    }
    return render(request, 'balloon/about.html', context)


def works(request):
    return HttpResponse("Наши работы")


def delivery(request):
    groups = Group.objects.all()
    context = {
        'title': 'Доставка',
        'menu': menu,
        'groups': groups,
    }
    return render(request, 'balloon/delivery.html', context)


def reviews(request):
    groups = Group.objects.all()
    context = {
        'title': 'Отзывы',
        'menu': menu,
        'groups': groups,
    }
    return render(request, 'balloon/reviews.html', context)


class Registration(DataMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'balloon/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        mixin_context = self.get_user_context(title='Регистрация')
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Logging(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'balloon/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Авторизация')
        finally_context = dict(list(context.items()) + list(mixin_context.items()))
        return finally_context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
