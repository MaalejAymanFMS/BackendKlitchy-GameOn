from django.db import models
from rest_framework import serializers

class User(models.Model):
    email = models.EmailField(primary_key=True)
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255,default="null")
    pin = models.CharField(unique=True,max_length=4)
    token=models.CharField(unique=True,max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'