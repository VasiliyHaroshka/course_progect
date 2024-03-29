from .telegramm import send_message
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .utils import *


class HomePage(Mixin, ListView):
    model = Balloon
    template_name = 'balloon/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Главная страница')
        return {**context, **mixin_context}

    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True)


class HomePageExpensiveFirst(HomePage):
    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True).order_by("-price")


class HomePageCheapFirst(HomePage):
    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True).order_by("price")


class HomePageOldFirst(HomePage):
    def get_queryset(self):
        return Balloon.objects.filter(is_onsite=True).order_by("time_modified")


class ShowGoodsInGroup(Mixin, ListView):
    model = Balloon
    template_name = "balloon/index.html"
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        group = Group.objects.get(slug=self.kwargs['group_slug'])
        mixin_context = self.get_user_context(title=str(group.name), group_selected=group.pk)
        return {**context, **mixin_context}

    def get_queryset(self):
        return Balloon.objects.filter(group__slug=self.kwargs['group_slug'], is_onsite=True)


class CertainProduct(Mixin, DetailView):
    model = Balloon
    template_name = 'balloon/show_product.html'
    slug_url_kwarg = 'good_slug'
    context_object_name = 'good'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=context['good'])
        return {**context, **mixin_context}


class AddProduct(Mixin, CreateView):
    form_class = AddProductForm
    template_name = 'balloon/add_product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Добавление товара на сайт')
        return {**context, **mixin_context}


def about(request):
    groups = Group.objects.all()
    allowed_menu = menu[:]
    white_box = Balloon.objects.get(slug='korobka-surpriz-belaia')
    color_box = Balloon.objects.get(slug='korobka-surpriz-tsvetnaya')
    lettering = Balloon.objects.get(slug='nadpisy-na-sharikah')
    if not request.user.is_superuser:
        allowed_menu.pop(4)
    context = {
        'title': 'О нас',
        'menu': allowed_menu,
        'groups': groups,
        'white_box': white_box,
        'color_box': color_box,
        'lettering': lettering,
    }
    return render(request, 'balloon/about.html', context)


def works(request):
    groups = Group.objects.all()
    allowed_menu = menu[:]
    if not request.user.is_superuser:
        allowed_menu.pop(4)
    context = {
        'title': 'Наши работы',
        'menu': allowed_menu,
        'groups': groups,
    }
    return render(request, 'balloon/works.html', context)


def delivery(request):
    groups = Group.objects.all()
    allowed_menu = menu[:]
    if not request.user.is_superuser:
        allowed_menu.pop(4)
    context = {
        'title': 'Доставка',
        'menu': allowed_menu,
        'groups': groups,
    }
    return render(request, 'balloon/delivery.html', context)


class Registration(Mixin, CreateView):
    form_class = RegistrationForm
    template_name = 'balloon/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        mixin_context = self.get_user_context(title='Регистрация')
        return {**context, **mixin_context}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('successfully')


class Logging(Mixin, LoginView):
    form_class = LoginForm
    template_name = 'balloon/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Авторизация')
        return {**context, **mixin_context}

    def get_success_url(self):
        return reverse_lazy('successfully')


def logout_user(request):
    logout(request)
    return redirect('home')


class Feedback(Mixin, FormView):
    form_class = FeedbackForm
    template_name = 'balloon/feedback.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title="Обратная связь")
        return {**context, **mixin_context}

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        information = form.cleaned_data['information']
        message = f"НОВОЕ СООБЩЕНИЕ!!!\n" \
                  f"ИМЯ: {str(name)}\n" \
                  f"ТЕЛЕФОН: {str(phone)}\n" \
                  f"ТЕКСТ: {str(information)}"
        send_message(message)
        return redirect('successfully')


def successfully(request):
    groups = Group.objects.all()
    allowed_menu = menu[:]
    if not request.user.is_superuser:
        allowed_menu.pop(4)
    context = {
        'title': 'Успешно',
        'menu': allowed_menu,
        'groups': groups,
    }
    return render(request, 'balloon/successfully.html', context)


def page_not_found(request, exception):
    return render(request, "error404.html")


def reviews(request):
    groups = Group.objects.all()
    form = LeaveReview
    allowed_menu = menu[:]
    if not request.user.is_superuser:
        allowed_menu.pop(4)
    if request.method == "POST":
        form = LeaveReview(request.POST, request.FILES)
        if form.is_valid():
            review = Review(
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                photo=form.cleaned_data['photo'],
            )
            review.save()
    all_reviews = Review.objects.all()
    context = {
        'title': 'Отзывы',
        'menu': allowed_menu,
        'groups': groups,
        "form": form,
        'all_reviews': all_reviews,
    }
    return render(request, 'balloon/reviews.html', context)





