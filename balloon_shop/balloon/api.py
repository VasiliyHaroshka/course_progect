from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import *
from rest_framework import generics
from rest_framework import filters


class ShowAllBalloonsAPI(generics.ListAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class ChangeBalloonAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer
    permission_classes = (IsAdminUser,)


class CreateBalloonAPI(generics.CreateAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer
    permission_classes = (IsAdminUser,)


class ShowAllGroupsAPI(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


class CreateGroupAPI(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (IsAdminUser,)


class ChangeGroupAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (IsAdminUser,)


class ShowAllReviewsAPI(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    filter_backends = [filters.OrderingFilter]


class CreateReviewAPI(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthenticated,)


class ChangeReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (IsAdminUser,)
