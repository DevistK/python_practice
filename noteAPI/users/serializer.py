from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from cards.serializer import CardSerializer

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','password',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(ModelSerializer):

    cards = CardSerializer(many=True, read_only=True)

    class Meta :
        model = User
        fields = ('id', 'username', 'password', 'cards')

        extra_kwargs = {'password': {'write_only': True}}
