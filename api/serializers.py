from rest_framework import serializers
from .models import User, Todo


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
