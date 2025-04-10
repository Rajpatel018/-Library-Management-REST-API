# library_app/library_api.py

from django.db import models
from rest_framework import serializers, viewsets
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ---------- Models ----------
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    issued_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    issued_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

# ---------- Serializers ----------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# ---------- ViewSets ----------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ---------- Routers and URLs ----------
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)

library_urls = [
    path('', include(router.urls)),
]
