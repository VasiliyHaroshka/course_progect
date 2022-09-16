from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
from .utils import *


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

    def get_context_data(self, *, object_list=None, groups=Group.objects.all(), **kwargs):
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


# def detail(request, good_slug):
#     good = get_object_or_404(Balloon, slug=good_slug)
#
#     context = {
#         'good': good,
#         'menu': menu,
#         'title': good.name,
#         'group_selected': good.group_id,
#     }
#
#     return render(request, 'balloon/show_product.html', context)


def works(request):
    return HttpResponse("Наши работы")


def delivery(request):
    return HttpResponse("Доставка")


def reviews(request):
    return HttpResponse("Отзывы")


def promocode(request):
    return HttpResponse("Промо-код")


def register(request):
    return HttpResponse("Регистрация")


def login(request):
    return HttpResponse("Войти")
