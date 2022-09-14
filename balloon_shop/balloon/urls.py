from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('good/<int:good_id>', detail, name='detail'),
    path('group/<int:group_id>', group, name='group'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('additional/', additional, name='additional'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('promocode/', promocode, name='promocode'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]