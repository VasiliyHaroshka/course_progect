from django.urls import path
from .views import *
from .api import *

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

    # API
    path('api/v1/balloons/', ShowAllBalloonsAPI.as_view(), name="show_balloons"),
    path('api/v1/create_balloon/', CreateBalloonAPI.as_view(), name="create_balloon"),
    path('api/v1/balloon/<int:pk>/', ChangeBalloonAPI.as_view(), name="change_balloon"),

    path('api/v1/groups/', ShowAllGroupsAPI.as_view(), name="show_groups"),
    path('api/v1/create_group/', CreateGroupAPI.as_view(), name="create_group"),
    path('api/v1/group/<int:pk>/', ChangeGroupAPI.as_view(), name="change_group"),

    path('api/v1/reviews/', ShowAllReviewsAPI.as_view(), name="show_reviews"),
    path('api/v1/create_review/', CreateReviewAPI.as_view(), name="create_review"),
    path('api/v1/review/<int:pk>/', ChangeReviewAPI.as_view(), name="change_review"),
]
