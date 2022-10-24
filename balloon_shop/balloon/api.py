from .serializers import *
from rest_framework import generics


class AllBalloonsAPI(generics.ListCreateAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer


class MasterBalloonAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balloon.objects.all()
    serializer_class = BalloonsSerializer


class AllGroupsAPI(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class MasterGroupAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


class AllReviewsAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class MasterReviewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
