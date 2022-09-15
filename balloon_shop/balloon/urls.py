from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('group/<slug:group_slug>', ShowGoodsInGroup.as_view(), name='group'),
    path('good/<slug:good_slug>', CertainProduct.as_view(), name='detail'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('additional/', additional, name='additional'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('promocode/', promocode, name='promocode'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]