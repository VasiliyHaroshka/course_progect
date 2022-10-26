from rest_framework.permissions import IsAdminUser
from .serializers import *
from rest_framework import generics


class ShowAllBalloonsAPI(generics.ListAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer


class ChangeBalloonAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer
    permission_classes = (IsAdminUser,)


class ShowAllGroupsAPI(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class ChangeGroupAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = (IsAdminUser,)


class ShowAllReviewsAPI(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class ChangeReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (IsAdminUser,)