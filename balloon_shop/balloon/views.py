from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
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


def index(request):
    goods = Balloon.objects.filter(is_onsite=True)
    groups = Group.objects.all()

    context = {
        'title': 'Главная страница',
        'menu': menu,
        'goods': goods,
        'groups': groups,
        'group_selected': 0,
    }
    return render(request, 'balloon/index.html', context)


def group(request, group_slug):
    goods = Balloon.objects.filter(group__slug=group_slug, is_onsite=True)
    groups = Group.objects.all()
    context = {
        'title': 'Категория товаров',
        'menu': menu,
        'goods': goods,
        'groups': groups,
        'group_selected': group_slug,
    }
    return render(request, 'balloon/index.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не существует!!!<h1>")


def about(request):
    groups = Group.objects.filter()
    context = {
        'title': 'Категория товаров',
        'menu': menu,
        'groups': groups,
    }
    return render(request, 'balloon/about.html', context)


def detail(request, good_slug):
    good = get_object_or_404(Balloon, slug=good_slug)

    context = {
        'good': good,
        'menu': menu,
        'title': good.name,
        'group_selected': good.group_id,
    }

    return render(request, 'balloon/show_product.html', context)


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
