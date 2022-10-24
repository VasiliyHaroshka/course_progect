from django.urls import path, include
from .views import *
from .api import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'all_balloons_api', AllBalloonsAPI)
router.register(r'all_groups_api', AllGroupsAPI)

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

    path('api/v1/allballoons/', AllBalloonsAPI.as_view(), name="all_balloons"),
    path('api/v1/balloon/<int:pk>/', MasterBalloonAPI.as_view(), name="certain_balloon"),
    path('api/v1/allgroups/', AllGroupsAPI.as_view(), name="all_groups"),
    path('api/v1/group/<int:pk>/', MasterGroupAPI.as_view(), name="update_group"),
    path('api/v1/allreviews/', AllReviewsAPI.as_view(), name="all_reviews"),
    path('api/v1/review/<int:pk>/', MasterReviewAPI.as_view(), name="update_review"),
]