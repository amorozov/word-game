from django.contrib.auth.models import  User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            User.EMAIL_FIELD,
            User.USERNAME_FIELD,
            'first_name',
            'last_name',
            'groups',
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]
