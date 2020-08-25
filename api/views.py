from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Todo
from .serializers import UserModelSerializer, TodoModelSerializer


class UsersHandler(APIView):

    def get(self, request):
        query = User.objects.all()
        serializers = UserModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK, template_name='rest_framework/admin.html')

    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetails(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = UserModelSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = UserModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersCheck(APIView):

    def get_object(self, username, password):
        try:
            return User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, username, password):
        article = self.get_object(username=username, password=password)
        serializer = UserModelSerializer(article)
        return Response(serializer.data)

    def put(self, request, username, password):
        article = self.get_object(username=username, password=password)
        serializer = UserModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, password):
        article = self.get_object(username=username, password=password)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoHandler(APIView):

    def get(self, request, id):
        query = Todo.objects.filter(userId=id)
        serializers = TodoModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK, template_name='rest_framework/admin.html')

    def post(self, request, id):
        serializer = TodoModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)