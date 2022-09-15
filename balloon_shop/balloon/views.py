from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *

menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Наши работы", "url_name": "works"},
    {"title": "Дополнительное оформление", "url_name": "additional"},
    {"title": "Доставка", "url_name": "delivery"},
    {"title": "Отзывы", "url_name": "reviews"},
    {"title": "Промо-код", "url_name": "promocode"},
    {"title": "Регистрация", "url_name": "register"},
    {"title": "Войти", "url_name": "login"},
]


class HomePage(ListView):
    model = Balloon
    template_name = 'balloon/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, groups=Group.objects.all(), **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Главная страница"
        context['groups'] = groups
        context['group_selected'] = 0
        return context

    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True)


class ShowGoodsInGroup(ListView):
    model = Balloon
    template_name = "balloon/index.html"
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, groups=Group.objects.all(), **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['goods'][0].group)
        context['groups'] = groups
        context['group_selected'] = context['goods'][0].group_id
        return context

    def get_queryset(self):
        return Balloon.objects.filter(group__slug=self.kwargs['group_slug'], is_onsite=True)


class CertainProduct(DetailView):
    model = Balloon
    template_name = 'balloon/show_product.html'
    slug_url_kwarg = 'good_slug'
    context_object_name = 'good'

    def get_context_data(self, *, object_list=None, groups=Group.objects.all(), **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['good']
        context['groups'] = groups
        return context


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


def additional(request):
    return HttpResponse("Дополнительное оформление")


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
