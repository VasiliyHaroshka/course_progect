from .models import *

menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Наши работы", "url_name": "works"},
    {"title": "Доставка", "url_name": "delivery"},
    {"title": "Отзывы", "url_name": "reviews"},
    {"title": "Промо-код", "url_name": "promocode"},
    {"title": "Добавить товар", "url_name": "add_product"},
    {"title": "Регистрация", "url_name": "register"},
    {"title": "Войти", "url_name": "login"},
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        groups = Group.objects.all()

        allowed_menu = menu.copy()
        if not self.request.user.is_superuser:
            allowed_menu.pop(5)
        # context['menu'] = allowed_menu

        if not self.request.user.is_authenticated:
            allowed_menu.pop(4)
        context['menu'] = allowed_menu

        context['groups'] = groups
        if 'group_selected' not in context:
            context['group_selected'] = 0
        return context
