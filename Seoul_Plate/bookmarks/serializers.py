from rest_framework import serializers, status
from rest_framework.response import Response

from restaurant.serializer import RestSerializer
from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    """ list: user_id, restaurant_id Serializer"""

    class Meta:
        model = BookMark
        fields = (
            'id',
            'restaurant',
            'bookmark_user',
        )
        read_only_fields = ['bookmark_user']


class UserBookMarkSerializer(serializers.ModelSerializer):
    """ 식당 정보 Serializer"""
    restaurant = RestSerializer(read_only=True)

    class Meta:
        model = BookMark
        fields = (
            'restaurant',
        )
