from .models import *

menu = [
    {"title": "О нас", "url_name": "about"},
    {"title": "Наши работы", "url_name": "works"},
    {"title": "Доставка", "url_name": "delivery"},
    {"title": "Отзывы", "url_name": "reviews"},
    {"title": "Промо-код", "url_name": "promocode"},
    {"title": "Добавить товар", "url_name": "add_product"},
]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        groups = Group.objects.all()

        allowed_menu = menu.copy()
        if not self.request.user.is_superuser:
            allowed_menu.pop(5)

        if not self.request.user.is_authenticated:
            allowed_menu.pop(4)
        context['menu'] = allowed_menu

        context['groups'] = groups
        if 'group_selected' not in context:
            context['group_selected'] = 0
        return context