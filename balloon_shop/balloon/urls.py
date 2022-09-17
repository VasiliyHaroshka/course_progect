from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('group/<slug:group_slug>', ShowGoodsInGroup.as_view(), name='group'),
    path('good/<slug:good_slug>', CertainProduct.as_view(), name='detail'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('promocode/', promocode, name='promocode'),
    path('register/', Registration.as_view(), name='register'),
    path('login/', login, name='login'),
]