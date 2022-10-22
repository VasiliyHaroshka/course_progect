from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('old_first/', HomePageOldFirst.as_view(), name='old_first'),
    path('expensive_first/', HomePageExpensiveFirst.as_view(), name='expensive_first'),
    path('cheap_first/', HomePageCheapFirst.as_view(), name='cheap_first'),
    path('group/<slug:group_slug>', ShowGoodsInGroup.as_view(), name='group'),
    path('good/<slug:good_slug>', CertainProduct.as_view(), name='detail'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('about/', about, name='about'),
    path('works/', works, name='works'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('register/', Registration.as_view(), name='register'),
    path('login/', Logging.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('successfully/', successfully, name='successfully'),
]