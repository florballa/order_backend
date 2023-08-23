from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Costumer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_active', 'groups']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['id', 'first_name', 'last_name', 'company_name']
