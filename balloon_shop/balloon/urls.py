from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('good/<slug:good_slug>', detail, name='detail'),
    path('group/<slug:group_slug>', group, name='group'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('additional/', additional, name='additional'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('promocode/', promocode, name='promocode'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]