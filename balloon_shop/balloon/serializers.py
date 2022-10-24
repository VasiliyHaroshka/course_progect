from .models import *
from rest_framework import serializers


class BalloonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balloon
        fields = ('id', 'name', 'description', 'price', 'photo', 'is_onsite', 'group')


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'text', 'photo')
